from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap
from django.utils.translation import ugettext as _

import markdown
from tagging.fields import TagField
from tagging.models import Tag
from photologue.models import Photo

class Entry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(                 
    unique_for_date = 'pub_date',
        help_text = 'Automatically build from the title.'
    )
    body_html = models.TextField(blank=True)
    body_markdown = models.TextField()
    image = models.ForeignKey(Photo, null=True)
    pub_date = models.DateTimeField('Date published') 
    tags = TagField()
    enable_comments = models.BooleanField(default = True)
    PUB_STATUS = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    status = models.IntegerField(choices=PUB_STATUS, default = 0)

    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
	verbose_name = (_('entry'))
        verbose_name_plural = (_('entries'))

    def __unicode__(self):
		return u'%s' %(self.title)

    def get_absolute_url(self):
        return "/%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    def save(self):
	import pdb
	pdb.set_trace()
        self.body_html = markdown.markdown(self.body_markdown, safe_mode = False)
        super(Entry, self).save()

