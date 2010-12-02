from django.conf.urls.defaults import *

urlpatterns = patterns('users.views',
    (r'^$', 'index'),
    (r'^signup/$', 'signup'),
    (r'^login/$', 'login'),
    (r'^signup/success/$', 'signup_success'),
    (r'^login/success/$', 'login_success'),
    (r'^(?P<profile_id>\d+)/$', 'view_profile'),
)
