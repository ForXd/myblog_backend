from rest_framework import viewsets

from ..serializers.post_serializer import PostSerializer, \
    FullPostSerializer, PartialPostSerializer
from ..models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PartialPostSerializer
        elif self.action == 'retrieve':
            return FullPostSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

