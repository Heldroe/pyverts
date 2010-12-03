#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_auth
from models import Profile
from cars.models import Car
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.utils.datastructures import MultiValueDictKeyError
from models import Profile
from forms import SignupForm, LoginForm, ProfileForm, NewCarForm, NewItineraryForm
from django.contrib.auth.decorators import login_required
from itinerary.models import Itinerary

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
    for i in range(len(cars)):
        #cars[i].ess_type = settings.ESSENCE_TYPES[cars[i].essence_type]
        cars[i].ess_type = settings.ESSENCE_TYPES[int(cars[i].essence_type)-1][1]
        cars[i].access = bool(cars[i].accessibility)
    return render_to_response('users/edit_cars.html',
            {'cars': cars})

@login_required
def edit_itineraries(request):
    itineraries = Itinerary.objects.filter(driver=request.user)
    return render_to_response('users/edit_itineraries.html',
            {'itineraries': itineraries})

@login_required
def add_itinerary(request):
    trip = Itinerary()
    if request.method == 'POST':
        form = NewItineraryForm(request.POST, instance=trip)
        if form.is_valid():
            trip.driver = request.user
            trip.save()
            return HttpResponseRedirect('/users/edit_itineraries/')
    else:
        form = NewItineraryForm(instance=trip)
    return render_to_response('users/add_itinerary.html', {'form': form},
            context_instance=RequestContext(request))

@login_required
def add_car(request):
    car = Car()
    if request.method == 'POST':
        form = NewCarForm(request.POST, instance=car)
        if form.is_valid():
            car.save()
            request.user.get_profile().cars.add(car)
            return HttpResponseRedirect('/users/edit_cars/')
    else:
        form = NewCarForm(instance=car)
    return render_to_response('users/add_car.html', {'form': form},
            context_instance=RequestContext(request))

@login_required
def delete_car(request, car_id):
    try:
        car = request.user.get_profile().cars.get(id=car_id)
        car.delete()
    except DoesNotExist:
        pass
    return HttpResponseRedirect('/users/edit_cars/')



def view_profile(request, profile_id):
    p = get_object_or_404(Profile, pk=profile_id)
    return render_to_response('users/profile.html', {'profile': p, 'lol' : p.cars.all()})
