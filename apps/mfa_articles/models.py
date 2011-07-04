# -*- coding: utf-8 -*-
import logging
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

# tranliteration for ru content
from pytils.translit import translify

# Get an instance of a logger
logger = logging.getLogger(__name__)


def strip(lst):
    return [x.strip() for x in lst]

class Category(models.Model):
    '''MFA article category'''
    title = models.CharField(max_length=100)
    slug = models.SlugField(editable=False)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translify(self.title))
        super(Category, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('mfa_articles:category-page', (), {
            'category_slug': self.slug,
            })

    def __unicode__(self):
        return self.title


class Article(models.Model):
    '''MFA article'''
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=255, blank=True)
    keywords = models.CharField(max_length=255, blank=True,
                                help_text="separate keywords by ','")
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False)
    content = models.TextField()

    category = models.ForeignKey(Category)
    pic = models.ImageField(upload_to="articles", blank=True)

    is_draft = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def get_keywords(self):
        if self.keywords:
            return strip(self.keywords.split(','))
        else:
            return ""

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translify(self.title))
        super(Article, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('mfa_articles:article-page', (), {
            'article_slug': self.slug,
            })

    def __unicode__(self):
        return self.title


class SiteCard(models.Model):
    '''General site information'''
    title = models.CharField(max_length=160)
    subtitle = models.CharField(max_length=160, blank=True)
    description = models.CharField(max_length=255, blank=True)
    keywords = models.CharField(max_length=255, blank=True,
                                help_text="separate keywords by ','")

    text = models.TextField(blank=True)

    class Meta:
        verbose_name = "SiteCard"
        verbose_name_plural = "SiteCard"

    def get_keywords(self):
        if self.keywords:
            return strip(self.keywords.split(','))
        else:
            return ""
