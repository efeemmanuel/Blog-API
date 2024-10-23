from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *





'''
the serializer is to convert the model instance(data) from a complex data types 

'''


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(view_name="blogapi:comments-detail", many=True, read_only=True)
    class Meta:
        model = Post
        fields = ["author", "post","comments","owner"]

class CommentSerializer(serializers.ModelSerializer):
    the_post = serializers.HyperlinkedRelatedField(view_name="blogapi:posts-detail", queryset=Post.objects.all())
    class Meta:
        model = Comment
        fields = ["comment", "the_post", "user"]