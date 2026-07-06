from django.urls import path, include
import posts.views as views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('favorites/', views.FavoritePostListView.as_view(), name='favorite_posts'),
    path('create', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),





]