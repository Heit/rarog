from django.conf import settings
from whoosh import store, fields
from whoosh.filedb.filestore import FileStorage
from whoosh import index
from os import environ
import os

environ['DJANGO_SETTINGS_MODULE'] = 'settings' 

from settings import *
from photologue.models import PhotoSize

userSmallThumb = PhotoSize(name = "userthumb", width = 77, height = 77, crop = True, pre_cache = False)
userSmallThumb.save()

slide = PhotoSize(name = "slide", width = 500, height = 250, crop = True, pre_cache = False )
slide.save()

thumbnail = PhotoSize(name = "thumbnail", width = 75, height = 75, pre_cache = True)
thumbnail.save()

display = PhotoSize(name = "display", width = 500, height = 240, pre_cache = False)
display.save()
 
