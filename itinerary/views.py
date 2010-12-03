#from django.template import Context, loader
from django.shortcuts import render_to_response
#from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from itinerary.models import Itinerary

def trajet_index(request):
  itineraries = Itinerary.objects.all()
  for i in range(len(itineraries)):
    itineraries[i].available_seats = 0 #itineraries[i].car.places - (itineraries[i].reserved_seats + len(itineraries[i].participant.all()) + 1)
  return render_to_response('itinerary/trajet_index.html', {'itineraries': itineraries})

def search(request):  
  
  return render_to_response('itinerary/search.html', {})

def sheet_itinerary(request, itinerary_id):
  itineraries = Itinerary.objects.get(id=itinerary_id)
  itineraries.available_seats = 0 # itineraries.car.places - (itineraries.reserved_seats + len(itineraries.participant.all()) + 1)
  return render_to_response('itinerary/sheet_itinerary.html', {'itinerary':itineraries})
