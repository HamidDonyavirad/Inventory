from rest_framework.views import APIView
from .serializers import RegisterSerializer,ProductSerializer,CategorySerializer,InventorySerializer,OrderSerializer,OrderItemSerializer
from rest_framework.response import Response
from .models import Product,Category,Inventory,Order,OrderItem
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'User created'},status=201)
        return Response(serializer.data, status=400)

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
        return Response(serializer.data, status=400) 
    
    def put(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.data, status=400) 
    
    def patch(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.data, status=400)
    
    def delete(self,request,pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=204)

class CategoryView(APIView):
    pass

class InventoryView(APIView):
    pass

class OrderView(APIView):
    pass

class OrderItemView(APIView):
    pass