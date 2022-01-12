from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag= models.CharField(max_length=100, default='basic blog')
    #content = models.TextField()
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title + ' | ' + self.author.username

    def get_absolute_url(self):
        return reverse('article_details',args=[str(self.id)])
