from django.contrib.sitemaps import Sitemap
from mfa_articles.models import Article

class ArticlesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Article.objects.filter(is_draft=False)[:5]
