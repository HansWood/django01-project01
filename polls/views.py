from django.http import HttpResponse
from django.shortcuts import render
# from django.shortcuts import redirect

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")