from django.urls import path

from . import views

urlpatterns = [
    path('', views.partners, name='partners'),
    #path('add_recipe/', views.add_recipe, name='add_recipe'),
    #path('recipe_update/<int:id>', views.recipe_update, name='recipe_update'),
    #path('recipe_delete/<int:id>', views.recipe_delete, name='recipe_delete'),
]
