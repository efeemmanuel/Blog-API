from django.db import models
from django.contrib.auth.models import User
# Create your models here.


'''
a model: the model is used to create a table in the database,(this is where the data's will be stored)
we need to create a post model (where the post are stored), then also a model for comments
'''

class Post(models.Model):
    author = models.CharField(max_length=30)  #field for the author
    post = models.TextField()     #field for the post
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # owner of the post

    def __str__(self):
        return f"{self.author} - {self.post}"   #function to convert to string
    


class Comment(models.Model):
    comment = models.CharField(max_length=100)        #field for the comment
    the_post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)    #field to map the comment to a post in the post model using a foreginkey(a many comment to one post)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    #user that made comment

    def __str__(self):
        return f"{self.comment} - {self.the_post}"   #function to convert to string