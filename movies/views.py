from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from movies.models import Tawain_movies_rank_2021

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

def index(request):
	title_name = "博雅通識小專題:電影資料分析"
	return render(request, 'index.html', locals())
# Create your views here.

def show(request):
    items = Tawain_movies_rank_2021.objects.all()
    return render(request, 'showpost.html', locals())

