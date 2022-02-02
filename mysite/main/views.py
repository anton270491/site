from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'main/index.html',{'title': 'Главная страница'})

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def work(request):
    return render(request,'main/work.html')
