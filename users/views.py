from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
  return HttpResponse("Index file !")

def signup(request):
  return render_to_response('users/signup.html')
