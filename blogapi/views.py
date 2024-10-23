from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.



class Postview(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Automatically set the owner to the authenticated user




class Commentview(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        post_id = self.request.data.get('post')  # Get the post ID from the request data
        try:
            post = Post.objects.get(id=post_id)  # Check if the post exists
            serializer.save(user=self.request.user, post=post)  # Save with the found post
        except Post.DoesNotExist:
            raise NotFound(detail="Post not found")  # Raise a 404 error if the post does not exist
