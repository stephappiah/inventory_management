from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


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


class ProductDetailApi(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
        try:
            return Product.objects.get(pk=self.kwargs.get('pk'))
        except ValueError:
            return Http404