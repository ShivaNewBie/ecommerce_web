from rest_framework import serializers 


from product.serializers import ProductSerializer
from .models import Checkout,CheckoutItem

class CheckoutItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta: 
        model = CheckoutItem
        fields = (
            "price",
            "product",
            "quantity",
        )

#list of checkout 
class CheckoutSerializer(serializers.ModelSerializer):
    items = CheckoutItemSerializer(many=True)

    class Meta:
        model = Checkout
        fields = ('created_by', 'name', 'email', 'phone', 'country'
        ,'address','city','zip','created_at','pay','stripe_token')