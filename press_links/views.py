from django.contrib.sites.models import Site
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from django_ajax.pagination import paginate

from press_links.models import Entry
from press_links.enums import DRAFT_STATUS, HIDDEN_STATUS


def entries(request):
    """
    A list of the entries.
    """

    context = {
        'object_list': paginate(request, Entry.objects.live()),
        'site_url': Site.objects.get_current().domain,
    }
    return render_to_response(
        'press_links/entry_list.html',
        context,
        context_instance=RequestContext(request)
    )


def entry(request, slug):
    """
    The detail view of an entry.
    """
    # Get entry
    obj = get_object_or_404(
        Entry, slug=slug, site=Site.objects.get_current()
    )
    should_raise_404 = (
        obj.status == DRAFT_STATUS and not
        request.user.is_staff or
        obj.status == HIDDEN_STATUS
    )
    if should_raise_404:
        raise Http404

    context = {
        'object': obj
    }
    return render_to_response(
        'press_links/entry_detail.html',
        context,
        context_instance=RequestContext(request)
    )
