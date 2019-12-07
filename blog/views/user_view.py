from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from blog.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from blog.serializers.user_serializer import PasswordSerializer, \
    LoginSerializer, UserSerializer, UserProfileSerializer


class LoginViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'login' or self.action == 'register':
            return LoginSerializer
        elif self.action == 'set_password':
            return PasswordSerializer
        return UserSerializer

    @action(detail=True, methods=['POST'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        print(user)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'success': 1})
        return Response({'success': 0, 'message': 'invalid password'})

    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(2)
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            if User.objects.filter(username=username):
                return Response({'success': 0, 'message': 'username exist'})
            user = User(username=username)
            user.set_password(password)
            user.save()
            return Response({'success': 1, 'token': user.token})
        return Response({'success': 0, 'message': 'invalid name or password'})

    @action(detail=False, methods=['POST'])
    @csrf_exempt
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({'success': 1, 'token': user.token})
        return Response({'success': 0, 'message': 'invalid name or password'})

    @action(detail=False, methods=['GET'])
    def logout(self, request):
        auth.logout(request)
        print('logout')
        return Response({'success': 1, 'message': ''})

    @action(detail=False)
    def recent_user(self, request):
        recent_users = User.objects.all().order_by('-last_login')
        page = self.paginate_queryset(recent_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_users, many=True)
        return Response(serializer.data)



