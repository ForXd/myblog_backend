from ..models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    toComment = serializers.PrimaryKeyRelatedField(allow_null=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['content', 'toPost', 'toComment']


class ReturnCommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    reply_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content',
                  'toPost', 'praiseNum', 'reply_comments']

