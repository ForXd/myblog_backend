from ..models import Post, Category
from rest_framework import serializers


class PartialPostSerializer(serializers.ModelSerializer):
    """
        return partial post
    """
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title',
                  'partial', 'postTime', 'praiseNum']


# two files self inference
from .category_serializer import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    """
        create post
    """
    title = serializers.CharField()
    category = CategorySerializer()
    content = serializers.CharField(trim_whitespace=False)

    # def validate_title(value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     if 'sb' in value.lower():
    #         raise serializers.ValidationError("post title illegal")
    #     return value

    def create(self, validated_data):
        category = validated_data.pop('category')
        category, created = Category.objects.get_or_create(name=category['name'])
        category.save()
        post = Post.objects.create(**validated_data, category=category)
        return post

    class Meta:
        model = Post
        fields = ['title', 'category', 'content']


class FullPostSerializer(serializers.ModelSerializer):
    """
        return full post
    """
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = CategorySerializer()
    post_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category',
                  'partial', 'content', 'postTime',
                  'praiseNum', 'post_comments']
