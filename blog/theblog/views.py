from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class Article(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddBlog(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(UpdateView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')