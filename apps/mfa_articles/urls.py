# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from mfa_articles.feed import ArticlesFeed

urlpatterns = patterns('mfa_articles.views',
    # rss and comments
    url(r'^feed/$', ArticlesFeed(), name="rssfeed"),

    url(r'^$', 'index', name='index-page'),
    url(r'^(?P<article_slug>.*)/$', 'article', name='article-page'),
    url(r'^category/(?P<category_slug>.*)$', 'category',
        name='category-page'),
)
