__author__ = 'ben'


from django.conf.urls import patterns, url

from views import SearchView

urlpatterns = patterns('',)
#App Specific


urlpatterns += patterns('', url( '^search$', SearchView.as_view(), name = 'search' ))
