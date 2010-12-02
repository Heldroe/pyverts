from django.conf.urls.defaults import *

urlpatterns = patterns('users.views',
    (r'^$', 'index'),
    (r'^signup/$', 'signup'),
    (r'^signup/success/$', 'signup_success'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

)
