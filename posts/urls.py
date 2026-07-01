from django.urls import path, include
import posts.views as views

urlpatterns = [
    path('', views.post_lists)
]