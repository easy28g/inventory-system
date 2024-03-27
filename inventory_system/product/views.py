from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProductSerializer
from .models import Product
from company.models import Company


class ProductViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        
        if not pk:
            return Product.objects.all()[:3]
        
        return Product.objects.filter(pk=pk)
    
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        company = Company.objects.get(pk=pk)
        return Response({'company': company.name})