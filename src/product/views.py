from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView 
from rest_framework.response import Response

from product.serializers import ProductSerializer


from .models import Product

class ProductListView(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()
        serializers = ProductSerializer(products,many=True)
        return Response(serializers.data)

class ProductDetail(APIView):
    def get(self,request,id):
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404