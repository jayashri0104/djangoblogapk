from django.shortcuts import render,get_object_or_404,redirect
#from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Article





    


def blog_detail(request,slug):
  article = get_object_or_404(Article, slug=slug)
  return render(request,'blog/blog_detail.html',{'article':article})



def like_post(request, slug):
        article = get_object_or_404(Article, slug=slug)
        article.likes += 1
        article.save()
        if request.user.is_authenticated:
            if request.user in article.likes.all():
                article.likes.remove(request.user)
            else:
               article.likes.add(request.user)
        return redirect('blog_detail', slug=slug) # Redirect back to the post detail pagefrom django.shortcuts import get_object_or_404, redirect


  
