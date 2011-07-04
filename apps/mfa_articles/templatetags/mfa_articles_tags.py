from mfa_articles.models import SiteCard
from django import template

register = template.Library()

@register.simple_tag()
def get_site_card():
    site_card = SiteCard.objects.get(id=1)
    return {"site_card_title": site_card.title,
            "site_card_description:": site_card.description}
