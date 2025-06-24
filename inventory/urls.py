from django.urls import path
from .views import RegisterView,ProductView, CategoryView, InventoryView, OrderView, OrderItemView, ProductStockView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('product/',ProductView.as_view(),name='product'),
    path('login/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('category/<int:pk>/',CategoryView.as_view(),name='category'),
    path('inventory/',InventoryView.as_view(),name='inventory'),
    path('inventory/stock/<int:pk>/', ProductStockView.as_view(), name='product-stock'),
]