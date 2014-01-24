from django.conf.urls import *

from press_links.models import Entry
from press_links.views import entries, entry

urlpatterns = patterns('',
    url(r'^$', entries, name='press_links_entry_list'),
    url(r'^(?P<slug>.*)/$', entry, name='press_links_entry_detail'),
)

