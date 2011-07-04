# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from mfa_articles.sitemap import ArticlesSitemap

sitemaps = {
    # put your app sitemap here
    'mfa_articles': ArticlesSitemap,
}


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}, name='sitemap'),

    url(r'', include('mfa_articles.urls', namespace='mfa_articles',
                     app_name='mfa_articles')),
)

# static urls will be disabled in production mode
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media\/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
