#coding: utf-8 
import re
from datetime import datetime
from collections import defaultdict
from django.shortcuts import render_to_response
from rarog.entries.models import Entry

MONTH_NAMES = ('', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август' ,
	       'Сентябрь', 'Октябрь', 'Декабрь')

def frontpage(request):
    entries, pagedata = init()
    return render_to_response('entries/list.html',pagedata)

def init():
    entries = Entry.objects.order_by('-pub_date').all()
    archive_data = get_year_map(entries)
    pagedata = {'page_data': archive_data,}
    return entries, pagedata

def create_archive_data(entries):
    archive_data = []
    count = {}
    mcount = {}
    for entry in entries:
        year = entry.pub_date.year
        month = entry.pub_date.month
        if year not in count:
            count[year] = 0
            mcount[year] = {}
        count[year] += 1
        if month not in mcount[year]:
            mcount[year][month] = 1
        else:
            mcount[year][month] += 1
    for year in sorted(count.iterkeys(), reverse = True):
        archive_data.append({'isyear':True,
                             'year': year,
                             'count': count[year],})
        for month in sorted(mcount[year].iterkeys(), reverse = True):
            archive_data.append({'isyear':False,
                                 'yearmonth': '%d/%02d' % (year, month),
                                 'monthname': MONTH_NAMES[month],
                                 'count': mcount[year][month],})
    return archive_data

def get_year_map(entries):
    result_data = []
    for entry in entries:
        result_data.append({'entry': entry, 
                            'yearmonth': '%d/%02d' % (entry.pub_date.year, entry.pub_date.month)})
    return result_data

