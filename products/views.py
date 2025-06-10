from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.exceptions import  NotFound
from django.db.models import Q
from products.CustomException import ProductOutOfStockException
from products.models import Products
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer, CategorySerializer, OrderDetailsSerializer


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
    # try:
    #     print("Open db connection - 37")
    #     data = Products.objects.filter(id=id).first()
    #     # if not data:
    #     #     raise ProductOutOfStockException("Product not found")
    #     serializedproduct = ProductSerializer(data)
    #     return Response(serializedproduct.data)
    # except Products.DoesNotExist as e:
    #     print("close db connection-44")
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    # except ProductOutOfStockException as ee:
    #     # raise Exception(ee)
    #     print(2)
    #     print(ee)
    #     print("close db connection-49")
    #     # return Response(status=status.HTTP_404_NOT_FOUND)
    #     try:
    #         raise Products.DoesNotExist()
    #     except Products.DoesNotExist:
    #         print("close db connection-54")
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    # except Exception as e:
    #     print(1)
    #     print(e)
    #     print("close db connection-59")
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    # finally:
    #     print("close db connection-62")
    try:
        data = Products.objects.get(id=id)
        # return Response(status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
    else:
        print("else")

@api_view(['POST'])
def create_product(request):
    try:
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_pricefilter_greater_product(request,price):
    try:
        print(price)
        output = Products.objects.filter(price__gte = price)
        serializedoutput = ProductSerializer(output, many=True)
        return Response(serializedoutput.data)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except ProductOutOfStockException as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_phonename_withfilter(request):
    # try:
    name_query = request.GET.get('name', default=None)
    # price_query = request.GET.get('price')
    # print(keyword.data)
    var = Q()
    if var:
        var &= Q(name__icontains=name_query)
    data = Products.objects.filter(var)
    serializedoutput = ProductSerializer(data, many=True).data
    # if serializedoutput.is_valid():
    return Response(serializedoutput, status=status.HTTP_200_OK)
    # return Response(serializedoutput.errors, status=status.HTTP_400_BAD_REQUEST)
    # except Exception as e:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_category(request):
    try:
        data = request.data
        serializeddata = CategorySerializer(data=data)
        if serializeddata.is_valid():
            serializeddata.save()
            return Response(serializeddata.data, status=status.HTTP_201_CREATED)
        return Response(serializeddata.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_orderdetails(request):
    try:
        data = request.data
        serializeddata = OrderDetailsSerializer(data=data)
        if serializeddata.is_valid():
            serializeddata.save()
            return Response(serializeddata.data, status=status.HTTP_201_CREATED)
        return Response(serializeddata.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)