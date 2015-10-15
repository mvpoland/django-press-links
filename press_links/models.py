from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from press_links.enums import STATUS_CHOICES, LIVE_STATUS, DRAFT_STATUS
from datetime import datetime


class EntryManager(models.Manager):
    def live(self):
        """
        Returns a list of all published entries.

        :rtype: django.db.models.QuerySet
        """
        return self.filter(pub_date__lte=datetime.now(), status=LIVE_STATUS).filter(site=Site.objects.get_current())


class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name=_('author'),
                               related_name='%(app_label)s_%(class)s_related')
    title = models.CharField(max_length=255, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, unique_for_date='pub_date', verbose_name='slug')
    pub_date = models.DateTimeField(default=datetime.now, verbose_name=_('publication date'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT_STATUS, verbose_name=_('status'))
    excerpt = models.TextField(blank=True, verbose_name=_(u'Excerpt'))
    source = models.CharField(max_length=255, verbose_name=_('the source for the entry'), blank=True)
    site = models.ManyToManyField(Site, verbose_name=_('Sites where the entry is published'), related_name='%(app_label)s_%(class)s_related')

    objects = EntryManager()

    @models.permalink
    def get_absolute_url(self):
        return ('press_links_entry_detail', (), {'slug': self.slug})

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-pub_date']
        verbose_name = _('Press Entry')
        verbose_name_plural = _('Press Entries')

    def __unicode__(self):
        return self.title


class Link(models.Model):
    link = models.CharField(max_length=255, verbose_name=_('link address (add http:// for external link)'))
    link_text = models.CharField(max_length=255, verbose_name=_('text for link'))
    link_new_page = models.BooleanField(default=False, verbose_name=_('open link in new page'))
    entry = models.ForeignKey(Entry, verbose_name=_('Entry'))

    class Meta:
        verbose_name = _('Press Link')
        verbose_name_plural = _('Press Links')
