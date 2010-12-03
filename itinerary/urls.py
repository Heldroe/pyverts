from django.conf.urls.defaults import *

urlpatterns = patterns('itinerary.views',
    (r'^$', 'trajet_index'),
    (r'^search/$', 'search'),
    (r'^sheet_itinerary/(?P<itinerary_id>\d+)/$', 'sheet_itinerary'),

)
