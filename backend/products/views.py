from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.self(user= self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
        # send a Django signal


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'
    # queryset = Product.objects.get


# product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.self(user= self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
        # send a Django signal

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


@api_view['GET', 'POST']
def product_alt_view(request, *args, **kwargs):
    method = request.method

    if method == "GET":
            # get request -> detail view
            # list view
            # url args??
            pass
    
    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            # data = serializer.data
            # instance = serializer.save()
            # print(instance)
            print(serializer.data)
            return Response(serializer.data) 
        return Response({"detail": "Not Good Data"}, status=400)
    

    

 
    
