from django.shortcuts import render
from django.http import HttpResponse
from .models import MenTshirt

def index(request):
    mens = MenTshirt.objects.all()
    return render(request,'index.html',{'mens':mens})
