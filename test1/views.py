from django.shortcuts import render, HttpResponse
from test1 import views

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("about page0")

def contact(request):
    return render(request, 'contact.html')