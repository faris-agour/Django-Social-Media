from posts.models import Post
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import PostSerializer


class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ["id"]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
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


