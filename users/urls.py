from django.conf.urls.defaults import *

urlpatterns = patterns('users.views',
    (r'^$', 'index'),
    (r'^signup/$', 'signup'),
    (r'^signup/success/$', 'signup_success'),

)
