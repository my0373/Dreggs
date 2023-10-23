from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    x = 1
    ct = request.content_type
    return render(request, "hello.html", {'message': request.content_type})