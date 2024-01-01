from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

from apps.preference.models import BannerModel, TopTendingProductsModel
from apps.product.models import CategoryModel, ProductModel
from apps.promotion.models import CampaignModel
from apps.blog.models import BlogModel


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


class ShopView(TemplateView):
    template_name = 'store/pages/shop.html'

    def get_context_data(self, **kwargs):
        context = {
            'categories': CategoryModel.objects.filter(is_active=True)
        }
        return context
