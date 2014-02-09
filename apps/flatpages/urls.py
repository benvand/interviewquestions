from django.conf.urls import patterns, include, url
from django.contrib.flatpages.views import flatpage

urlpatterns = patterns('',)



urlpatterns += patterns('',
                        url('^about/$',
                            flatpage,
                            {'url': '/about/'},
                             name='about'
                            )
                        )

urlpatterns += patterns('',
                        url('^contact/$',
                            flatpage,
                            {'url': '/contact/'},
                            name='contact'
                            )
                        )
