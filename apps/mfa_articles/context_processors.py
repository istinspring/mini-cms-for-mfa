import logging
from django.shortcuts import get_object_or_404
from mfa_articles.models import SiteCard, Article, Category

# Get an instance of a logger
logger = logging.getLogger(__name__)


def mfa_context(request):
    '''Global variables'''
    if '/admin/' in request.path:
        return {}
    
    site_card = get_object_or_404(SiteCard, id=1)
    
    return {
        'mfa_site': site_card,
        'mfa_categories': Category.objects.all()
    }
