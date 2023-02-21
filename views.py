from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializers, CategorySerializers, ProductSerializers, BasketSerializers
from .models import UsersModel, CategoryModel, ProductModel, BasketModel
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class UsersView(ModelViewSet):
    queryset = UsersModel.objects.all()
    serializer_class = UserSerializers


class CategoryView(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers


class ProductView(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers


class AllCategories(APIView):

    def get(self, request):
        data = CategoryModel.objects.all()
        serializer = CategorySerializers(data, many=True)
        return Response(serializer.data)


class ProductsByCategory(APIView):

    def get(self, request, pk):
        data = ProductModel.objects.filter(category_id=pk)
        serializer = ProductSerializers(data, many=True)
        return Response(serializer.data)


class BasketView(ModelViewSet):
    queryset = BasketModel.objects.all()
    serializer_class = BasketSerializers
