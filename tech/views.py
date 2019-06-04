# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import KindofEarly,KindofMid,KindofLate
import json
# Create your views here.

def zsdata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = KindofEarly.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
    js = []
    cd = len(list)
    if cd != 0:
        for var in list:
            js.append({'id': var.id, 'title': var.title})
        jsobj = {'tit': js}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    else:
        return HttpResponse('')

def zsread(req):
    num = req.GET.get('num')
    res = KindofEarly.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def zhongshudata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = KindofMid.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
    js = []
    cd = len(list)
    if cd != 0:
        for var in list:
            js.append({'id': var.id, 'title': var.title})
        jsobj = {'tit': js}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    else:
        return HttpResponse('')

def zhongshuread(req):
    num = req.GET.get('num')
    res = KindofMid.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def wsdata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = KindofLate.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
    js = []
    cd = len(list)
    if cd != 0:
        for var in list:
            js.append({'id': var.id, 'title': var.title})
        jsobj = {'tit': js}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    else:
        return HttpResponse('')

def wsread(req):
    num = req.GET.get('num')
    res = KindofLate.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)
