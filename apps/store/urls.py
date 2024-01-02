from django.urls import path

from apps.store.views import HomeView, ShopView, ProductView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<str:uuid>/', ProductView.as_view(), name='product-details'),
]