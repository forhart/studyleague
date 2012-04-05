from django.conf.urls import patterns, include, url
from studyleague import settings
import ckeditor 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from sl_pre.views import stream_list,plan_list, semester_list
urlpatterns = patterns('',
    (r'^ckeditor/',include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,'show_indexes':True}), 

#below was used for dojo's editor
#(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
#                        {'document_root': '/home/windeor/arel/studyleague/studyleague/media/', 'show_indexes': True}),
                      
    (r'^$',stream_list),
    (r'^plans/',plan_list),

     url(
        r'^(?P<stream_slug>[^/]+)',semester_list
        ),                   
    


    #site_media url 

  

          # Examples:

    # url(r'^$', 'studyleague.views.home', name='home'),
    # url(r'^studyleague/', include('studyleague.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     

     
)

