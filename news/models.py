from django.db import models
from django.utils.translation import ugettext as _

import datetime

class SiteNew(models.Model):
    title = models.TextField(_('title'), max_length=80, blank=True)
    descriptn = models.TextField(_('descriptn'), max_length=255, blank=True)
    eventdate = models.DateField(_('eventdate'), null=True)
    pubdate = models.DateField(_('pubdate'))
    organizer = models.TextField(_('organizer'), null=True)
    orgsite = models.URLField(_('orgsite'), null=True)

    class Meta:
        ordering = ('-pubdate',)
        verbose_name = (_('sitenew'))
        verbose_name_plural = (_('sitenews'))

    def save(self):
        self.pubdate = datetime.datetime.now()
        super(SiteNew, self).save()

	
