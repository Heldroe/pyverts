from django.conf.urls.defaults import *

urlpatterns = patterns('itineraries.views',
    (r'^$', 'trajet_index'),
    (r'^search/$', 'search'),
    (r'^(?P<itinerary_id>\d+)/view/$', 'view_itinerary'),
)
