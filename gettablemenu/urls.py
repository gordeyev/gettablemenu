from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from menu import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^menu/', include('menu.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
