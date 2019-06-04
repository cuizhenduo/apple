# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,render_to_response,redirect
from django import forms
from .models import wenzhang
import json
# Create your views here.
def downapk(req):
    return render_to_response('downapk.html', {'blog': 'blog', 'form': 'form', 'id': 'id', 'tag': 'tag'})

def test(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    list = wenzhang.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
    cd = len(list)
    js = []
    if cd != 0:
        for var in list:
            js.append({'id':var.id,'title':var.title})
        jsobj = {'tit':js}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    else:
        return HttpResponse('')

def readnews(req):
    num = req.GET.get('num')
    res = wenzhang.objects.get(id=num)
    jsobj = {'title':res.title,'article':res.article}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)
