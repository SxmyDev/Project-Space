from django.shortcuts import render

def home(request):
    context = {}
    return render(request,'eclipse/home.html',context)