#-*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.utils.datastructures import MultiValueDictKeyError

from models import Profile
from forms import SignupForm, LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Index file !")

def signup_success(request):
    return render_to_response('users/signup_success.html')

def login_success(request):
    return render_to_response('users/login_success.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['name'],"",form.cleaned_data['password'])
            user.save()
            profile = Profile(user=user)
            profile.save()
            return HttpResponseRedirect('success/')
    else:
        form = SignupForm()

    return render_to_response('users/signup.html',
            {'form': form},
            context_instance=RequestContext(request))

def login(request):
    nextPage = False
    try:
        nextPage = request.GET['next']
        url_out = '/users/login/?next=' + nextPage
    except MultiValueDictKeyError:
        url_out = '/users/login/'
        pass
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['name'], password=form.cleaned_data['password'])
            login_auth(request, user)
            # Redirect to a success page.
            if nextPage:
                return HttpResponseRedirect(nextPage)
            return HttpResponseRedirect('success/')
    else:
        form = LoginForm()

    return render_to_response('users/login.html',
            {'form': form, 'url_out': url_out},
            context_instance=RequestContext(request))

def logout(request):
    logout_auth(request)
    return HttpResponse("Logged out")


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.get_profile())
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user.get_profile())

    return render_to_response('users/edit_profile.html',
            {'form': form},
            context_instance=RequestContext(request))

@login_required
def edit_cars(request):
    cars = request.user.get_profile().cars.all()
    return render_to_response('users/edit_cars.html',
            {'cars': cars})

@login_required
def add_car(request):
    if request.method == 'POST':
        car = Car()
        form = NewCarForm(request.POST, instance=car)
        if form.is_valid():
            print form
            print car
    return HttpResponse("Logged out")
