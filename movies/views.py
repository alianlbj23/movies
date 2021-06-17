from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from movies.models import rank_chapion_world

def index(request):
	title_name = "博雅通識小專題:電影資料分析"
	return render(request, 'index.html', locals())
# Create your views here.

def show(request):
    items = rank_chapion_world.objects.all()
    a = 123
    return render(request, 'showpost.html', locals())
    

