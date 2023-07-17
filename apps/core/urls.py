from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.eportal, name='eportal'),
    path('recipes/', include('apps.recipes.urls'), name = 'recipes'),
    path('products/', include('apps.products.urls'), name = 'products'),
    path('partners/', include('apps.partners.urls'), name = 'partners'),
]
