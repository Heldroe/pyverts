from django.conf.urls.defaults import *

urlpatterns = patterns('users.views',
    (r'^$', 'index'),
    (r'^signup/$', 'signup'),
    (r'^edit_profile/$', 'edit_profile'),
    (r'^login/$', 'login'),
    (r'^logout/$', 'logout'),
    (r'^signup/success/$', 'signup_success'),
    (r'^login/success/$', 'login_success'),
    (r'^profile/(?P<profile_id>\d+)/$', 'view_profile'),
)
