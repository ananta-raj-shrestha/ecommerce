from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"shop/index.html")
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("contact")
def tracker(request):
    return HttpResponse("tracker")
def view(request):
    return HttpResponse("product")
def cart(request):
    return HttpResponse("cart")
def search(request):
    return HttpResponse("search")