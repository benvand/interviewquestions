from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views
from django.views.generic import RedirectView


#Don't put them here. Make sections and append
urlpatterns = patterns('',)

#Admin
admin.autodiscover()

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    )

#Stuff to serve static admin content
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)
urlpatterns += staticfiles_urlpatterns()

#comingsoon
#urlpatterns += patterns('', url( '^$', views.comingSoon, name='ComingSoon' ))



#Apps

#Dev only. Implicit on development machines
if settings.DEV:
    urlpatterns += patterns('', url('',include('app.quest.urls')),)

#Prod Final structure
elif settings.PROD:
    pass
    # urlpatterns += patterns('', url('^contact/',include('contact.urls')),)

#static 
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)
urlpatterns += staticfiles_urlpatterns()

#media
urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT,}))

#Error Pages
if not settings.DEV:
    handler500 = views.fiveHundred
    handler404 = views.fourHundred

