# Datatrans registry
from datatrans.utils import register
from press_links.models import Entry, Link


class PressEntryTranslation(object):
    fields = ('title', 'excerpt', 'source')
register(Entry, PressEntryTranslation)


class LinkTranslation(object):
    fields = ('link', 'link_text')
register(Link, LinkTranslation)
