from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.all_products, name='all'),
    path('add/', views.add_product, name='add'),
    path('<int:pk>/', views.product_detail, name='detail'),
    path('<int:pk>/edit/', views.edit_product, name='edit'),
    path('<int:pk>/delete/', views.delete_product, name='delete'),
    path('<int:pk>/stock/', views.update_stock, name='update_stock'),
    path('subcategory/<int:subcategory_pk>/', views.product_list, name='list'),
]