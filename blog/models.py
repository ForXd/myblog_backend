from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt
from backend import settings


class Category(models.Model):
    name = models.CharField(max_length=50)

class User(AbstractUser):
    avatar = models.CharField(max_length=500, blank=True, null=True)
    focus = models.ForeignKey('self', related_name='follower_users',
                              null=True, blank=True, on_delete=models.SET_NULL)
    followers = models.ForeignKey('self', related_name='focus_users',
                                  null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token = jwt.encode({
            'user': {
                'username': self.username
            }
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


class Post(models.Model):
    author = models.ForeignKey(to=User, related_name='user_posts', on_delete=models.CASCADE)
    title = models.CharField(default=False, max_length=200)
    category = models.ForeignKey(to=Category, null=True, blank=True,
                                 related_name='category_posts', on_delete=models.SET_NULL)
    content = models.TextField()
    partial = models.CharField(default='', max_length=300)
    postTime = models.DateTimeField(auto_now_add=True)
    praiseNum = models.IntegerField(default=0)

    class Meta:
        ordering = ['praiseNum']


class Comment(models.Model):
    author = models.ForeignKey(to=User, related_name='user_comments', on_delete=models.CASCADE)
    toPost = models.ForeignKey(to=Post, related_name='post_comments', on_delete=models.CASCADE)
    content = models.TextField()
    toComment = models.ForeignKey('self', related_name='reply_comments',
                                  null=True, blank=True, on_delete=models.SET_NULL)
    praiseNum = models.IntegerField(default=0)

    class Meta:
        ordering = ['praiseNum']


class Message(models.Model):
    content = models.CharField(default='', max_length=300)
    fromUser = models.ForeignKey(to=User, related_name='send_user', on_delete=models.CASCADE)
    toUser = models.ForeignKey(to=User, related_name='receive_user', on_delete=models.CASCADE)


# Create your models here.
