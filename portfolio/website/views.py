from django.shortcuts import render
import requests

# Create your views here.
def Index(request):
    return render(request, template_name = "website/index.html")


