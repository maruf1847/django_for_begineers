from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
	return HttpResponse("<h1>Hello World,this is our home</h1>")
