from django.urls import path, include
from rest_framework import routers
from blog.views import user_view
from blog.views import post_view
from blog.views import comment_view
from blog.views import message_view
from blog.views import category_view

router = routers.DefaultRouter()
router.register(r'users', user_view.LoginViewSet)
router.register(r'posts', post_view.PostViewSet)
router.register(r'comments', comment_view.CommentViewSet)
router.register(r'messages', message_view.MessageViewSet)
router.register(r'categorys', category_view.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]