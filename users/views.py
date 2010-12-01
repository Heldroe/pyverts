from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
  return HttpResponse("Index file !")

def signup(request):
  try:
    name = request.POST['name']
  except KeyError:
    return render_to_response('users/signup.html', {
        'err_msg': "You must set a name"},
        context_instance=RequestContext(request)
        )
  try:
    password = request.POST['password']
    password2 = request.POST['password2']
  except KeyError:
    return render_to_response('users/signup.html', {
        'err_msg': "You must set a password"},
        context_instance=RequestContext(request)
        )
  else:
    if password != password2:
      return render_to_response('users/signup.html', {
          'err_msg': "Passwords must be the same"},
          context_instance=RequestContext(request)
          )
    else:
      return render_to_response('users/signup_success.html')
  return render_to_response('users/signup.html')

