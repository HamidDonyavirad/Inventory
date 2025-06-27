from rest_framework.views import APIView
from .serializers import RegisterSerializer,ProductSerializer,CategorySerializer,InventorySerializer,OrderSerializer,OrderItemSerializer
from rest_framework.response import Response
from .models import Product,Category,Inventory,Order,OrderItem
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Sum
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'User created'},status=201)
        return Response(serializer.errors, status=400)


class ProductView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201) 
        return Response(serializer.errors, status=400) 
    
    def put(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400) 
    
    def patch(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=204)


class CategoryView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=201)
    
    def post(self,request):
        serializer= CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def put(self,request,pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=204)
            
            
class InventoryView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        category = Inventory.objects.get(pk=pk)
        category.delete()
        return Response(status=204)

class OrderView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        category = Order.objects.get(pk=pk)
        category.delete()
        return Response(status=204)

class OrderItemView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        orderitem = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderitem,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer= OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self,request,pk):
        category = OrderItem.objects.get(pk=pk)
        category.delete()
        return Response(status=204)
    
class ProductStockView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'Product not found'}, status=404)
        
        inbound = Inventory.objects.filter(product=product, transaction_type='inbound').aggregate(Sum('quantity'))['quantity__sum'] or 0
        outbound = Inventory.objects.filter(product=product, transaction_type='outbound').aggregate(Sum('quantity'))['quantity__sum'] or 0

        current_stock = inbound - outbound

        return Response({
            'product': product.product_name,
            'product_id': product.id,
            'stock': current_stock
        })
                
 
class LogoutView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        refresh_token = request.data.get("refresh")
        if refresh_token is None:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST) 
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  
            return Response({"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError as e:
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)          