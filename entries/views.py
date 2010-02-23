#coding: utf-8 
import re
import calendar
from datetime import date
from collections import defaultdict
from django.shortcuts import render_to_response
from rarog.entries.models import Entry

MONTH_NAMES = ('', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Фвгуст' ,
	       'Сентябрь', 'Ноябрь', 'Декабрь')

def frontpage(request):
    year = request.GET.get('year', date.today().year)
    month = request.GET.get('month', date.today().month)
    basedate = date(year, month, calendar.monthrange(year, month)[1])
    pagedata = init(basedate)
    return render_to_response('entries/list.html',pagedata)

def init(basedate):
    entries = Entry.objects.order_by('-pub_date').all()
    archive_data = get_year_map(entries)
    pagedata = {'page_data': archive_data,
                'entries': entries,}
    return pagedata

def get_year_map(entries):
    result_data = []
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
        result_data.append({'isyear':True,
                             'year': year,
                             'count': count[year],})
        for month in sorted(mcount[year].iterkeys(), reverse = True):
            result_data.append({'isyear':False,
                                'yearmonth': '%d/%02d' % (year, month),
                                'monthname': MONTH_NAMES[month],
                                'count': mcount[year][month],})
    return result_data

