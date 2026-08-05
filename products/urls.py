from django.urls import path
from. import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/create/', views.create_product, name='create-product'),
    path('products/<int:pk>/', views.update_product, name='update-product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete-product'),
]