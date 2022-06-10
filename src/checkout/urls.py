from django.urls import path 

from .views import CheckoutList, checkout


urlpatterns = [
    path('checkout/',checkout,name='checkout'),
    path('checkout-order/', CheckoutList.as_view()),  

]