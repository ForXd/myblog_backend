from rest_framework import viewsets

from ..serializers.category_serializer import ReturnCategorySerializer
from ..models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ReturnCategorySerializer


    