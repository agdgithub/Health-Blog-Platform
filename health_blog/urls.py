# blog/urls.py
from django.urls import path
from blog import views


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.user_login, name='login'),  # Login page
    path('logout/', views.user_logout, name='logout'),  # Logout page
    path('add_article/', views.add_article, name='add_article'),  # Add article page
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]

