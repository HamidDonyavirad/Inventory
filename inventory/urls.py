from django.urls import path
from .views import RegisterView,ProductsView, CategoryView, InventoryView, OrderView, OrderLineView, ProductStockView,LogoutView, ProductsDetailView,CategoryDetailView,InventoryDetailView,OrderDetailView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('products/',ProductsView.as_view(),name='products'),
    path('products/<int:pk>/',ProductsDetailView.as_view(),name='product-detail'),
    path('category/',CategoryView.as_view(),name='category'),
    path('category/<int:pk>/',CategoryDetailView.as_view(),name='category-detail'),
    path('inventory/',InventoryView.as_view(),name='inventory'),
    path('inventory/<int:pk>/',InventoryDetailView.as_view(),name='inventory-detail'),
    path('inventory/stock/<int:pk>/', ProductStockView.as_view(), name='product-stock'),
    path('order/',OrderView.as_view(),name='order'),
    path('order/<int:pk>/',OrderDetailView.as_view(),name='order-detail'),
    path('orderline/',OrderLineView.as_view(),name='orderline'),
]