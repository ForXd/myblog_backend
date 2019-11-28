from rest_framework import viewsets
from ..models import Comment
from ..serializers.comment_serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)
