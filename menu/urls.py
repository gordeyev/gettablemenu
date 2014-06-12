from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from menu import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.menu_ru, name='menu-ru-urls'),
)
