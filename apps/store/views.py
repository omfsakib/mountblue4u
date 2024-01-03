import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.db.models import Min, Max
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.preference.models import BannerModel, TopTendingProductsModel
from apps.product.models import CategoryModel, ProductModel, SizeModel, ColorModel
from apps.promotion.models import CampaignModel, DeliveryChargeModel
from apps.blog.models import BlogModel
from apps.product.filters import ProductFilter
from apps.sales.models import Order, OrderItem


class HomeView(TemplateView):
    template_name = 'store/pages/home.html'

    def get_context_data(self, **kwargs):
        context = {
            'banners': BannerModel.objects.filter(is_active=True),
            'top_trending_products': TopTendingProductsModel.objects.last().products.all()[:8],
            'featured_categorys': CategoryModel.objects.filter(is_active=True, is_featured=True),
            'new_arrivals': ProductModel.objects.filter(is_active=True).order_by('-created_at')[:8],
            'campaigns': CampaignModel.objects.filter(is_active=True).order_by('-created_at')[:2],
            'blogs': BlogModel.objects.filter(is_active=True).order_by('-created_at'),
        }

        return context


from django.views import View


class ShopView(View):
    template_name = 'store/pages/shop.html'
    filterset_class = ProductFilter

    def get(self, request, *args, **kwargs):
        showing_products = 16
        products = ProductModel.objects.all()
        products_filter = self.filterset_class(request.GET, queryset=products)
        filtered_products = products_filter.qs

        total_products = len(filtered_products)

        lowest_price = products.aggregate(lowest_price=Min('price'))
        highest_price = products.aggregate(highest_price=Max('price'))

        lowest_price_value = lowest_price['lowest_price']
        highest_price_value = highest_price['highest_price']

        applied_category_filters = request.GET.getlist('category')  # Get selected category filters as a list
        applied_size_filters = request.GET.getlist('size')
        if request.GET.get('show'):
            showing_products = int(request.GET.get('show'))

        if showing_products > total_products:
            showing_products = total_products

        context = {
            'categories': CategoryModel.objects.filter(is_active=True),
            'sizes': SizeModel.objects.filter(is_active=True),
            'colors': ColorModel.objects.filter(is_active=True),
            'lowest_price': lowest_price_value,
            'highest_price': highest_price_value,
            'products': filtered_products[:showing_products],
            'applied_filters': {
                'category': applied_category_filters,
                'size': applied_size_filters,
                'color': request.GET.get('color'),
                'order_by': request.GET.get('order_by')
            },
            'showing_products': showing_products,
            'total_products': total_products
        }
        return render(request, self.template_name, context)


class ProductView(View):
    template_name = 'store/pages/product-details.html'
    model = ProductModel

    def get(self, request, *args, **kwargs):
        uuid = kwargs.get('uuid')
        product = ProductModel.objects.get(uuid=uuid)
        related_products = ProductModel.objects.filter(category=product.category).exclude(uuid=product.uuid)
        context = {
            'product': product,
            'related_products': related_products
        }

        return render(request, self.template_name, context)


class CartView(View):
    template_name = 'store/pages/cart.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class CheckoutView(View):
    template_name = 'store/pages/checkout.html'

    def get(self, request, *args, **kwargs):
        context = {
            'delivery_charge': DeliveryChargeModel.objects.last()
        }
        return render(request, self.template_name, context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productID']
    action = data['action']
    color = data['color']
    size = data['size']
    quantity = data['quantity']

    customer = request.user
    product = ProductModel.objects.get(uuid=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if size and color != "undefined":
        orderItem.color = color
        orderItem.size = size

    if quantity == 'undefined':
        quantity = 1

    orderItem.price = product.price

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + int(quantity))

    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    elif action == 'delete':
        orderItem.quantity = 0

    elif action == 'color':
        orderItem.color = color

    elif action == 'size':
        orderItem.size = size

    orderItem.total = (orderItem.quantity * product.price)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
