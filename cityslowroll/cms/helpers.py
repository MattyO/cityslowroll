from cms.models import Page
from django.db.models import Q
def nav():
    return { 'pages': Page.objects.filter(Q(active=True), ~Q(slug='index') ) }
