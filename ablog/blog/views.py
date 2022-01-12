from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Post
from .forms import PostForm,EditForm


# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    context_object_name = 'post'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','content']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = '/'

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request,category):
    category_name = Category.objects.get(name=category)
    category_post= Post.objects.filter(category=category_name)
    return render(request, 'category.html', {'category':category,'category_post':category_post})