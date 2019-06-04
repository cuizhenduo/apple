# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BuildY
from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
def buildydata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = BuildY.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
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

def buildyread(req):
    num = req.GET.get('num')
    res = BuildY.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)