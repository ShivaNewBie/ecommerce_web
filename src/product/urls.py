
from django.urls import path ,include

from .views import ProductListView, ProductDetail, CategoryDetail

urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='product-serializer'),
    path('product/<int:id>/', ProductDetail.as_view(),name='product-detail' ),
    path('product/<slug:category_slug>/', CategoryDetail.as_view(),name='category-detail' ),
]