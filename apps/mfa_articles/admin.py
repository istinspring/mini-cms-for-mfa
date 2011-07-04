from django.contrib import admin
from mfa_articles.models import Article, SiteCard, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description',
                    'keywords', 'pub_date', 'content')
    search_field = ('title', 'slug')

    class Media:
        js = [
            '/static/tiny_mce/tiny_mce.js',
            '/media/common_js/tinymce_setup.js',
        ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    search_field = ('title', 'slug')

    class Media:
        js = [
            '/static/tiny_mce/tiny_mce.js',
            '/media/common_js/tinymce_setup.js',
        ]


class SiteCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'keywords', 'text')

    class Media:
        js = [
            '/static/tiny_mce/tiny_mce.js',
            '/media/common_js/tinymce_setup.js',
        ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SiteCard, SiteCardAdmin)
