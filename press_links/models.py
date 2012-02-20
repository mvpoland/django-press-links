import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models
from press_links.enums import STATUS_CHOICES, LIVE_STATUS, DRAFT_STATUS

class EntryManager(models.Manager):
    def live(self):
        """
        Returns a list of all published entries.

        :rtype: django.db.models.QuerySet
        """
        return self.filter(status=LIVE_STATUS).filter(site=Site.objects.get_current())

class Entry(models.Model):
    author = models.ForeignKey(User, verbose_name=_('author'), related_name='%(app_label)s_%(class)s_related')
    title = models.CharField(max_length=255, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, unique_for_date='pub_date', verbose_name='slug')
    pub_date = models.DateTimeField(default=datetime.datetime.now, verbose_name=_('publication date'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS, verbose_name=_('status'))
    excerpt = tinymce_models.HTMLField(blank=True, verbose_name=_('excerpt'))
    source = models.CharField(max_length=255, verbose_name=_('the source for the entry'), blank=True)
    site = models.ManyToManyField(Site, verbose_name=_('Sites where the entry is published'), related_name='%(app_label)s_%(class)s_related')

    objects = EntryManager()

    @models.permalink
    def get_absolute_url(self):
        return ('press_links_entry_detail', (), {'slug': self.slug})

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-pub_date']
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')

    def __unicode__(self):
        return self.title

class Link(models.Model):
    link = models.CharField(max_length=255, verbose_name=_('link address'))
    link_text = models.CharField(max_length=255, verbose_name=_('text for link'))
    entry = models.ForeignKey(Entry, verbose_name=_('Entry'))
