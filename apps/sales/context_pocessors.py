from apps.product.models import ProductModel
from apps.sales.models import Order


def get_context(request):
    orders = Order.objects.filter(complete=True)
    top_selling_products = ProductModel.objects.filter(is_active=True).order_by('-sell_count')

    context = {
        'total_orders': orders.count(),
        'pending': orders.filter(status=Order.OrderStatus.customer_confirmed).count(),
        'confirmed': orders.filter(status=Order.OrderStatus.admin_confirmed).count(),
        'delivered': orders.filter(status=Order.OrderStatus.delivered).count(),
        'in_transit': orders.filter(status=Order.OrderStatus.in_transit).count(),
        'return': orders.filter(status=Order.OrderStatus.in_return).count(),
        'cancel': orders.filter(status=Order.OrderStatus.cancel).count(),
        'top_selling_products': top_selling_products,
    }
    return context
