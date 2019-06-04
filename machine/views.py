# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Machine
from django.http import HttpResponse
import json
# Create your views here.
def machinedata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    response = ''
    #list = wenzhang.objects.all()
    list = Machine.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
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

def machineread(req):
    num = req.GET.get('num')
    res = Machine.objects.get(id=num)
    jsobj = {'title': res.title, 'article': res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)