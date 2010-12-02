#from django.template import Context, loader
from django.shortcuts import render_to_response
#from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from itinerary.models import Itinerary

def trajet_index(request):
  itineraries = Itinerary.objects.all()
  return render_to_response('itinerary/trajet_index.html', {'itineraries': itineraries})
