from django.shortcuts import render
#from django.views.generic import TemplateView
from django.views.generic import ListView
#from django.template import TemplateView
from .models import Post

# Create your views here.
""""
class HomePageView(TemplateView):
    template_name = "home.html"
    model = Post
"""
class HomePageView(ListView):
    template_name = "home.html"
    model = Post