from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from sl_pre.views import stream_list,plan_list, semester_list
urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),                     
    (r'^$',stream_list),
    (r'^plans/',plan_list),
   url(
        r'^(?P<stream_slug>[^/]+)',semester_list),                   
    # Examples:
    # url(r'^$', 'studyleague.views.home', name='home'),
    # url(r'^studyleague/', include('studyleague.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     

     
)

