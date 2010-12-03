from django.conf.urls.defaults import *

urlpatterns = patterns('users.views',
    (r'^$', 'index'),
    (r'^signup/$', 'signup'),
    (r'^edit_profile/$', 'edit_profile'),
    (r'^login/$', 'login'),
    (r'^logout/$', 'logout'),
    (r'^signup/success/$', 'signup_success'),
    (r'^login/success/$', 'login_success'),
    (r'^edit_cars/$', 'edit_cars'),
    (r'^edit_cars/delete/(\d+)/$', 'delete_car'),
    (r'^edit_cars/add/$', 'add_car'),
    (r'^edit_itineraries/$', 'edit_itineraries'),
    (r'^edit_itineraries/add/$', 'add_itinerary'),
    (r'^profile/(?P<profile_id>\d+)/$', 'view_profile'),
)
