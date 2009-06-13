import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

#admin and login/logout
urlpatterns = patterns('',
  (r'^admin/(.*)', admin.site.root),
  (r'^accounts/login/$',  login),
  (r'^accounts/logout/$', logout),
)

#static content for development
if settings.DEBUG:
  urlpatterns += patterns('',
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
  )
