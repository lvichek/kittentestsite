from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import task



 

def hello_mainpage(request):

    tasks = task.objects.all()

    return render(request, 'mainpage.html', 
    {'title':'main page', 'tasks': tasks} )  


def about(request):
    return HttpResponse("<h4>hello this is my about method</h4>")

def cool_page(request):
    return render(request, 'cool_page.html')  

def addition(request):
    return render(request, 'addition.html')   

def get_json(request):  

    import requests

    url = 'bcs_tester:iLoveBCS@45.32.232.25:3669'
    payload = {}

    return  

"""
def add(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2

    return render(request, 'result.html', {'result':res})     
"""
def add_post(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, 'result_post.html', {'result':res})       