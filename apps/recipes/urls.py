from django.urls import path
from django.conf import settings #add this
from django.conf.urls.static import static #add this


from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe_update/<int:id>', views.recipe_update, name='recipe_update'),
    path('recipe_delete/<int:id>', views.recipe_delete, name='recipe_delete'),
]


# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
