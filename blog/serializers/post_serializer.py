from ..models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """
        create post
    """
    title = serializers.CharField()
    category = serializers.CharField()
    content = serializers.CharField()

    # def validate_title(value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     if 'sb' in value.lower():
    #         raise serializers.ValidationError("post title illegal")
    #     return value

    class Meta:
        model = Post
        fields = ['title', 'category', 'content']


class PartialPostSerializer(serializers.ModelSerializer):
    """
        return partial post
    """
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category',
                  'partial', 'postTime', 'praiseNum']


class FullPostSerializer(serializers.ModelSerializer):
    """
        return full post
    """
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category',
                  'partial', 'content', 'postTime',
                  'praiseNum', 'comments']
