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

slide = PhotoSize(name = "slide", width = 600, height = 250, crop = True, pre_cache = False )
slide.save()



 
