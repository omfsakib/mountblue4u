from django.urls import path

from apps.store.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]