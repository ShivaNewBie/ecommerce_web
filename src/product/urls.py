
from django.urls import path ,include

from .views import ProductListView, ProductDetail

urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='product-serializer'),
    path('product/<int:id>/', ProductDetail.as_view(),name='product-detail' )
]