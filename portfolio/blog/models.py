from django.db import models
from django.contrib.auth.models import User 

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to="blog/")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='article_like')
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
   
    
    
   
