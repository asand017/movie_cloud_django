from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# will have just the index view for this project

def index(request):
	return HttpResponse("Movie Cloud init page")
