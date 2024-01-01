from django.urls import path

from apps.store.views import HomeView, ShopView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
]