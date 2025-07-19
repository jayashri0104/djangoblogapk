from django.urls import path
from . import views


urlpatterns = [

    
  
    
   
    
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/like/<slug:slug>/', views.like_post, name='like_article'),
 
]

