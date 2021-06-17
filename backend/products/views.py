from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated


class ProductCreateApi(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListApi(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class =ProductSerializer


class ProductUpdateApi(generics.RetrieveUpdateAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteApi(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer