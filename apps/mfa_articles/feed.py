from django.contrib.syndication.views import Feed
from mfa_articles.models import Article
from config import FEED_TITLE, FEED_DESCRIPTION

class ArticlesFeed(Feed):
    title = FEED_TITLE
    link = "/"
    description = FEED_DESCRIPTION

    def items(self):
        return Article.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
