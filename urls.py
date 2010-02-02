import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.simple import direct_to_template

admin.autodiscover()

#defaults -- index, admin, login, logout, profile
urlpatterns = patterns('',
  (r'^$', direct_to_template, {
    'template': 'index.html'
  }),
  (r'^admin/(.*)', include(admin.site.urls)),
  (r'^accounts/login/$',  login),
  (r'^accounts/logout/$', logout),
  (r'^accounts/profile/$', direct_to_template, {
    'template': 'registration/profile.html'
  }),
)

#static content for development
if settings.DEBUG:
  urlpatterns += patterns('',
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
  )
