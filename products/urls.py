from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('new product/', views.ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update product/', views.ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete product/', views.ProductDelete.as_view(), name='product_delete'),
]
