from django.urls import path
from .views import RegisterView,ProductView, CategoryView, InventoryView, OrderView, OrderItemView




urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('product/',ProductView.as_view(),name='product'),
    
]