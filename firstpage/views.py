#coding: utf-8
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from whoosh import index, fields
from whoosh.filedb.filestore import FileStorage
from whoosh.qparser import QueryParser
from rarog.users.models import UserProfile
from rarog.news.models import SiteNew
from rarog.firstpage.models import PageEntry, PageImage
from rarog.entries.management.commands.createindex import WHOOSH_SCHEMA


def index(request):
    pagedata = init(request)
    return render_to_response('firstpage/pageentry_list.html', pagedata,    context_instance=RequestContext(request))

def init(request):
    profile_items = UserProfile.objects.order_by('?')[0:1]
    profile_item = None
    if len(profile_items) > 0:
        profile_item = profile_items[0]
    hits = search(request)
    pagedata = {'pageitems' : PageEntry.objects.all(),
                'pageimages' : PageImage.objects.all(),
                'sitenews' : SiteNew.objects.order_by('pubdate')[:5],
                'hits': hits,
                'profile': profile_item,
    }
    return pagedata

def search(request):
    storage = FileStorage(settings.WHOOSH_INDEX)
    ix = storage.open_index(indexname="rarog")
    hits = []
    query = request.GET.get('q', None)
    if query is not None and query != u"":
        query = query.replace('+', ' AND ').replace(' -', ' NOT ')
        parser = QueryParser("body_html", schema=ix.schema)
        try:
            qry = parser.parse(query)
        except:
            qry = None
        if qry is not None:
            searcher = ix.searcher()
            hits = searcher.search(qry)
    return hits






    

	

