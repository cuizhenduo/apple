from django.shortcuts import render
from .models import zhuanjia
from django.http import HttpResponse
import json
# Create your views here.
def proflogin(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    try:
        res = zhuanjia.objects.get(profname=username)
    except :
        return HttpResponse('nouser')

    pwd = res.password
    if password == pwd:
        return HttpResponse('ok')
    else:
        return HttpResponse('noeq')

def showprof(req):
    # 初始化
    res = []
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = zhuanjia.objects.all()
    for var in list:
        res.append(var.profname)
    jsobj = {'proname': res}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)