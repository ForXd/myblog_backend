from ..models import Category
from rest_framework import serializers
from .post_serializer import PartialPostSerializer


class CategorySerializer(serializers.ModelSerializer):
    """
        create category
    """
    name = serializers.CharField()

    class Meta: 
        model = Category
        fields = ['name']


class ReturnCategorySerializer(serializers.ModelSerializer):
    """
        return category
    """
    name = serializers.CharField()
    category_posts = PartialPostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'category_posts']