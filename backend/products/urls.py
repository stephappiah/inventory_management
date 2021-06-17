from django.urls import path
from .views import ProductCreateApi, ProductListApi, ProductUpdateApi, ProductDeleteApi, ProductDetailApi


urlpatterns = [
    path('create/', ProductCreateApi.as_view(), name='create-product'),
    path('list/', ProductListApi.as_view(), name='list-product'),
    path('update/<int:pk>/', ProductUpdateApi.as_view(), name='update-product'),
    path('<int:pk>/delete/', ProductDeleteApi.as_view(), name='delete-product'),
    path('<int:pk>/view/', ProductDetailApi.as_view(), name='view-product')
]