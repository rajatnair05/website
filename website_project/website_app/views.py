from django.shortcuts import render
from django.http import HttpResponse

def website(request):
    return render(request, 'website.html')

def contact(request):
    return render(request, 'contact_us.html')

def about(request):
    return render(request, 'about_us.html')