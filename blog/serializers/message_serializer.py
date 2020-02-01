from ..models import Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    content = serializers.CharField()

    class Meta:
        model = Message
        fields = ['content', 'fromUser', 'toUser']