from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request=request,
            template_name="main/home.html")

def resume(request):
    return render(request=request,
            template_name="main/resume.html")

def blog(request):
    return render(request=request,
            template_name="main/lb/2019.html")

def blog_post(request, post):
    return render(request=request,
            template_name="main/lb/blog/" + post)
