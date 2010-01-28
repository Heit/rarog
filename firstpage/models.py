#coding: utf-8 
from django.db import models
from photologue.models import Photo
from django.utils.translation import ugettext as _

import markdown

class PageEntry(models.Model):
    body_html = models.TextField(blank=True)
    body_mrk = models.TextField(_('body'))
    dataorder = models.PositiveIntegerField(_('dataorder'), default = 1)

    class Meta:
        ordering = ('-dataorder',)
        get_latest_by = 'dataorder'
	verbose_name = u'Заглавный параграф'
	verbose_name_plural = u'Заглавные параграфы'

    def save(self):
        self.body_html = markdown.markdown(self.body_mrk, safe_mode = False)
        super(PageEntry, self).save()

class PageImage(models.Model):
    image = models.ForeignKey(Photo)
    dataorder = models.PositiveIntegerField(_('dataorder'), default = 1)

    class Meta:
        ordering = ('-dataorder',)
        get_latest_by = 'dataorder'
	verbose_name = _('pageimage')
	verbose_name_plural = _('pageimages')
	

