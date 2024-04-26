import datetime
from django.contrib.auth.models import User
import jwt
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .serializers import UserSerializer  # Import your UserSerializer here


class RegisterAPIView(APIView):
    def post(self, request):
        # instead of form we use serializer And don't forget to hash password
        request.data['password'] = make_password(request.data["password"])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Save the validated data to create a new user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class loginAPIView(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        # Check if user with provided username exists
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        # Token and Cookie
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm="HS256")
        res = Response()
        res.set_cookie(key='jwt', value=token, httponly=True)
        res.data = {
            "jwt": token
        }
        return res


class UserInfo(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise serializers.ValidationError("Can't Authenticate")
        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError("Expired token")
        user = User.objects.filter(id=payload['id']).first()
        serialize = UserSerializer(user)
        return Response(serialize.data)

class logoutAPIView(APIView):
    def post(self,request):
        res = Response()
        res.delete_cookie('jwt')
        res.data = {"success log out"}
        return res



class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ["id"]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['user__username', 'body']
    ordering_fields = ["created"]


class PostDetailsApiView(generics.RetrieveAPIView):
    queryset = Post.objects.all()  # Remove this line
    serializer_class = PostSerializer
    lookup_field = 'id'


class PostAddApiView(generics.CreateAPIView):
    queryset = Post.objects.all()  # Remove this line
    serializer_class = PostSerializer


class PostEditApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()  # Remove this line
    serializer_class = PostSerializer
    lookup_field = 'id'
