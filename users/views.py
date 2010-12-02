from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
  return HttpResponse("Index file !")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/signup/success/')
    else:
        form = SignupForm()

    return render_to_response('users/signup.html', {
        'form': form,
    })

