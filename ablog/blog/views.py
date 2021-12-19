from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    context_object_name = 'post'