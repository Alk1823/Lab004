from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

taxRate = 0.15

def index(request):
    return render(request,'Taxapp/index.html')

def newPrice(request,number):
    tax = taxRate * number
    number = number + tax
    return HttpResponse(f'Price after tax {number}')

def taxrate(request):
    return render(request,"Taxapp/display.html",{"taxRate":str(taxRate)})

