from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User


from forms import SignupForm

def index(request):
    return HttpResponse("Index file !")

def signup_success(request):
    return render_to_response('users/signup_success.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['name'], form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('success/')
    else:
        form = SignupForm()

    return render_to_response('users/signup.html',
            {'form': form},
            context_instance=RequestContext(request))

