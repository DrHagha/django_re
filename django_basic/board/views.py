from django.shortcuts import render

def boardfirst(request):
    return render(request, 'boardfirst.html')

def boardlist(request):
    return render(request, 'boardlist.html')