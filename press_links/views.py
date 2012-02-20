import datetime

from django.conf import settings
from django.contrib.sites.models import Site
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from press_links.models import Entry
from press_links.enums import DRAFT_STATUS, HIDDEN_STATUS, LIVE_STATUS, MONTH_NAMES

from templatable_view import templatable_view
from django_ajax.pagination import paginate


@templatable_view('press_links/entry_list.html')
def entries(request):
    """
    A list of the entries.
    """

    return {
        'object_list': paginate(request, Entry.objects.live()),
    }


@templatable_view('press_links/entry_detail.html')
def entry(request, slug):
    """
    The detail view of an entry.
    """
    # Get entry
    object = get_object_or_404(Entry, slug=slug, site=Site.objects.get_current())
    if object.status == DRAFT_STATUS and not request.user.is_staff or object.status == HIDDEN_STATUS:
        raise Http404

    # Context
    return {
        'object':object
    }

