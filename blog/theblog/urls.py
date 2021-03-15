from django.urls import path
from .views import HomeView, Article, AddBlog, UpdatePostView, DeletePostView, AddCategory, CategoryView
# from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', Article.as_view(), name="article-detail"),
    path('add_post/', AddBlog.as_view(), name="add_post"),
    path('add_category/', AddCategory.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
]