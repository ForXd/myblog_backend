from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['POST'])
    def by_list(self, request):
        print(request.data)
        comments = Comment.objects.filter(pk__in=request.data)
        page = self.paginate_queryset(comments)
        if page is not None:
            ser = self.get_serializer(page, many=True)
            return self.get_paginated_response(ser.data)
        ser = self.get_serializer(comments, many=True)
        return Response(ser.data)
