from django.conf.urls.defaults import *

urlpatterns = patterns('itinerary.views',
    (r'^$', 'trajet_index'),
    (r'^search/$', 'search'),
    (r'^view/(?P<itinerary_id>\d+)/$', 'view_itinerary'),
)
