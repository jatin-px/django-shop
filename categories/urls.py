from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.category_list, name='list'),
    path('add/', views.add_category, name='add'),
    path('<int:pk>/edit/', views.edit_category, name='edit'),
    path('<int:pk>/delete/', views.delete_category, name='delete'),
    path('<int:category_pk>/subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/add/', views.add_subcategory, name='subcategory_add'),
    path('subcategories/<int:pk>/edit/', views.edit_subcategory, name='subcategory_edit'),
    path('subcategories/<int:pk>/delete/', views.delete_subcategory, name='subcategory_delete'),
]