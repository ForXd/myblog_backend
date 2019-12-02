from rest_framework import viewsets
from ..models import Comment
from ..serializers.comment_serializer import CommentSerializer, ReturnCommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ReturnCommentSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)
