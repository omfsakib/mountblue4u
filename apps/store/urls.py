from django.urls import path

from apps.store.views import HomeView, ShopView, ProductView, updateItem, CartView, CheckoutView, MyAccountView, \
    WishListView, BlogListView, BlogDetailsView, SubscriptionPostView, PageView, InvoiceView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<str:uuid>/', ProductView.as_view(), name='product-details'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('myaccount/', MyAccountView.as_view(), name='my-account'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('page/<str:slug>/', PageView.as_view(), name='page'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blog/<str:uuid>/', BlogDetailsView.as_view(), name='blog-details'),
    path('invoice/<str:uuid>/', InvoiceView.as_view(), name='invoice'),
    path('subscribe/', SubscriptionPostView.as_view(), name='subscribe'),
    path('update_item/', updateItem, name='update-item'),
]