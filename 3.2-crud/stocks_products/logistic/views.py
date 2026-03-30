from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ["title", "description"]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer  # (queryset, many=True)
    # при необходимости добавьте параметры фильтрации
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ["products__title", "products__description"]
