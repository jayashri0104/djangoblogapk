from django.shortcuts import render
from blog.models import Article

# Create your views here.
def Index(request):
    Articles=Article.objects.all()
    return render(request, "website/index.html",{'articles':Articles})


