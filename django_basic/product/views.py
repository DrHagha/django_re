from django.shortcuts import render

def productfirst(request):
    return render(request, 'productfirst.html')

def productlist(request):
    return render(request, 'productlist.html')