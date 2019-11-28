from ..models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate_title(value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value

    class Meta:
        model = Post
        fields = ['author', 'title', 'category', 'partial', 'content', 'postTime', 'praiseNum']
