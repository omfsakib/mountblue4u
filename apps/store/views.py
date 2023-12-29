from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

from apps.preference.models import BannerModel, TopTendingProductsModel
from apps.product.models import CategoryModel, ProductModel
from apps.promotion.models import CampaignModel


class HomeView(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context = {
            'banners': BannerModel.objects.filter(is_active=True),
            'top_trending_products': TopTendingProductsModel.objects.last().products.all()[:8],
            'featured_categorys': CategoryModel.objects.filter(is_active=True, is_featured=True),
            'new_arrivals': ProductModel.objects.filter(is_active=True).order_by('-created_at')[:8],
            'campaigns': CampaignModel.objects.filter(is_active=True).order_by('-created_at')[:2]
        }
        # Add any additional context data here if needed
        return context
