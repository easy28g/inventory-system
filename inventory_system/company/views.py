from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        
        if not pk:
            return Company.objects.all()[:3]
        
        return Company.objects.filter(pk=pk)