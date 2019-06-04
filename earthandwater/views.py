# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Earth,Shifei,Water
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def earthdata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = Earth.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
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

def earthread(req):
    num = req.GET.get('num')
    res = Earth.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)


def shifeidata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = Shifei.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
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

def shifeiread(req):
    num = req.GET.get('num')
    res = Shifei.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)



def waterdata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = Water.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
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

def waterread(req):
    num = req.GET.get('num')
    res = Water.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)