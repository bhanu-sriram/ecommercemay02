from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from products.models import Products
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.
def hello(request):
    data = Products.objects.all()
    d = data[0]
    print(d.name)
    d.name = 'iphone'
    d.save()
    print(d.name)
    return HttpResponse('Hello World!')


## GET method
@api_view(['GET'])
def get_products(request):
    data = Products.objects.all()
    serializedproducts = ProductSerializer(data, many=True)
    return Response(serializedproducts.data)

@api_view(['GET'])
def get_product_by_id(request, id):
    try:
        data = Products.objects.get(id=id)
        serializedproduct = ProductSerializer(data)
        return Response(serializedproduct.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_product(request):
    try:
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)