from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('Hello world')

def hr(request):
	return HttpResponse('remembering')

def hk(request):
	return HttpResponse('remring')