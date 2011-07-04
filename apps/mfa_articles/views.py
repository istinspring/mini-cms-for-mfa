# -*- coding: utf-8 -*-
from django.shortcuts import redirect, get_object_or_404, render
from django.core.urlresolvers import reverse
from django.conf import settings

from mfa_articles.models import Article, Category, SiteCard


def index(request):
    ''' Get all articles'''
    all_articles = Article.objects.filter(is_draft=False)
    return render(request, 'index.html', {'articles': all_articles,})
                                         

def article(request, article_slug):
    _article = get_object_or_404(Article, slug=article_slug)
    return render(request, 'article.html', {'article': _article})


def category(request, category_slug):
    _category = get_object_or_404(Category, slug=category_slug)
    articles = _category.article_set.filter(is_draft=False)
    return render(request, 'category.html', {'articles': articles,
                                             'category': _category})
