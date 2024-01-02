from django.urls import path

from apps.store.views import HomeView, ShopView, ProductView, updateItem, CartView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<str:uuid>/', ProductView.as_view(), name='product-details'),
    path('cart/', CartView.as_view(), name='cart'),
    path('update_item/', updateItem, name='update-item'),
]