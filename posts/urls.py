from django.urls import path, include
import posts.views as views

urlpatterns = [
    path('/posts', views.post_lists)
]