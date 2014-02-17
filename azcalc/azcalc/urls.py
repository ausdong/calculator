from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', include('calc.urls')),
    url(r'^calc/thecalc$', include('calc.urls')),
    # Examples:
    # url(r'^$', 'azcalc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

)
