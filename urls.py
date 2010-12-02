from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    # Example:
    # (r'^pyverts/', include('pyverts.foo.urls')),
    (r'^users/', include('users.urls')),
    (r'^$', 'direct_to_template', {'template': 'index.html'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
