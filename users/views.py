from django.shortcuts import render_to_response
from rarog.users.models import UserProfile
from rarog.news.models import SiteNew
from rarog.firstpage.models import PageEntry, PageImage
from django.template import RequestContext

def index(request):
    pagedata = init()
    return render_to_response('firstpage/pageentry_list.html', pagedata,    context_instance=RequestContext(request))

def init():
    profile_items = UserProfile.objects.order_by('?')[0:1]
    profile_item = None
    if len(profile_items) > 0:
        profile_item = profile_items[0]
    pagedata = {'pageitems' : PageEntry.objects.all(),
                'pageimages' : PageImage.objects.all(),
                'sitenews' : SiteNew.objects.all(),
                'profile': profile_item,
    }
    return pagedata
