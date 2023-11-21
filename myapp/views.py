from django.shortcuts import render
from django.http import HttpResponse
#from .models import Musics, myVideo, Category
from .models import Dashdetail
from django.views.generic import ListView, DetailView
from django.db.models import Q

class Dashboard(ListView):
  model = Dashdetail
  template_name = "dashboard.html"
  context_object_name = "dashboard"