import django_filters
from django.db.models import Q

from apps.product.models import ProductModel, CategoryModel, SizeModel, ColorModel

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.ModelMultipleChoiceFilter(field_name='category', queryset=CategoryModel.objects.all())
    size = django_filters.ModelMultipleChoiceFilter(field_name='product_variants__size',
                                                    queryset=SizeModel.objects.all())
    color = django_filters.ModelChoiceFilter(field_name='product_variants__color', queryset=ColorModel.objects.all())
    q = django_filters.CharFilter(method='search_products')

    ORDER_CHOICES = (
        ('', 'Default'),
        ('rating_asc', 'Rating: Low to High'),
        ('rating_desc', 'Rating: High to Low'),
        ('price_asc', 'Price: Low to High'),
        ('price_desc', 'Price: High to Low'),
    )

    order_by = django_filters.ChoiceFilter(label='Order By', choices=ORDER_CHOICES, method='filter_order_by')

    class Meta:
        model = ProductModel
        fields = ['min_price', 'max_price', 'category', 'size', 'color']

    def search_products(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(description__icontains=value) | Q(product_variants__code__icontains=value)
        )

    def filter_order_by(self, queryset, name, value):
        if value == 'rating_asc':
            return queryset.order_by('rating')
        elif value == 'rating_desc':
            return queryset.order_by('-rating')
        elif value == 'price_asc':
            return queryset.order_by('price')
        elif value == 'price_desc':
            return queryset.order_by('-price')
        else:
            return queryset