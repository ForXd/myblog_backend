from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers.post_serializer import PostSerializer, \
    FullPostSerializer, PartialPostSerializer
from ..models import Post
import markdown


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

    @action(detail=True, methods=['GET'])
    def get_markdown_content(self, request, pk=None):
        post = self.get_object()
        md = markdown.Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_content = md.convert(post.content)
        context = {'md': md_content, 'toc': md.toc}
        return Response(context)

