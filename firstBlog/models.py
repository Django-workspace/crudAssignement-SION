from tkinter import CASCADE
from django.db import models
import uuid
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Blog(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.CharField(max_length=100,null=True,blank=False)
    createdDate=models.DateTimeField(auto_now_add=True)
    
    
    def get_total_likes(self):
        return self.blog_likes__count()
    def __str__(self):
        return str(self.title)
    
class BlogLikes(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    users=models.ManyToManyField(User, related_name="likees")
    blog=models.OneToOneField(Blog, related_name="blog_likes",on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)