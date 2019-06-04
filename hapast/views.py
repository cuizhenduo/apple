# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Cao,Chong,Bing
from django.http import HttpResponse
import json
# Create your views here.
def chongdata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = Chong.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
    cd = len(list)
    js = []
    if cd != 0:
        for var in list:
            js.append({'id': var.id, 'title': var.title})
        jsobj = {'tit': js}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    else:
        return HttpResponse('')

def chongread(req):
    num = req.GET.get('num')
    res = Chong.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def bingdata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = Bing.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
    cd = len(list)
    js = []
    if cd != 0:
        for var in list:
            js.append({'id': var.id, 'title': var.title})
        jsobj = {'tit': js}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    else:
        return HttpResponse('')

def bingread(req):
    num = req.GET.get('num')
    res = Bing.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def caodata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = Cao.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
    cd = len(list)
    js = []
    if cd != 0:
        for var in list:
            js.append({'id': var.id, 'title': var.title})
        jsobj = {'tit': js}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    else:
        return HttpResponse('')

def caoread(req):
    num = req.GET.get('num')
    res = Cao.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)