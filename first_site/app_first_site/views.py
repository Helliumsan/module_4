from django.shortcuts import render
from app_first_site.models import Advertisement
from django.http import HttpResponse

# Create your views here.

def index(request):
    advertisements= Advertisement.objects.all()
    context={'advertisements': advertisements}
    return render(request, 'advertisement/index.html',context)

def top_sellers(request):
    return render(request, 'advertisement/top-sellers.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def login(request):
    return render(request, 'auth/login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'auth/register.html')

