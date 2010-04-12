from django.conf import settings
from whoosh import store, fields
from whoosh.filedb.filestore import FileStorage
from whoosh.analysis import StemmingAnalyzer
from django.db.models import signals
from rarog.entries.models import models as entry_models
from django.core.management.base import NoArgsCommand, CommandError
from whoosh import index
import os
import sys

WHOOSH_SCHEMA = fields.Schema(title=fields.TEXT(stored=True),
                              body_html=fields.TEXT(analyzer=StemmingAnalyzer()),
                              url=fields.ID(stored=True, unique=True))

def create_index():
    if not os.path.exists(settings.WHOOSH_INDEX):
        os.makedirs(settings.WHOOSH_INDEX)
    storage = FileStorage(settings.WHOOSH_INDEX)
    storage.create_index(schema=WHOOSH_SCHEMA, indexname="rarog")


class Command(NoArgsCommand):
    help = "Creates full-text index for Rarog-Site application named rarog"
    requires_model_validation = False
    def handle_noargs(self, **options):
        try:
            create_index()
            print "Initial Whoosh index in directory '%s' created" % (settings.WHOOSH_INDEX)
        except Exception as err:
            print 'Error in index: ', err
            raise CommandError("Can't create full-text index")






