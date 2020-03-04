from django.urls import path
from . import views

app_name = "methylation"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("click_point/", views.click_point, name="click_point"),
    # path("rss.xml", views.rss, name="rss"),
    # path("resume/", views.resume, name="resume"),
    # path("blog/", views.blog, name="blog"),
    # path("blog/<str:post>", views.blog_post, name="blog_post"),
    
]
