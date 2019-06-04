from django.shortcuts import render
from .models import luntan
from prof.models import zhuanjia
from django.http import HttpResponse
import json
# Create your views here.
def setpnum(req):
    num = int(req.GET.get('num', None))
    username = req.GET.get('username', None)
    res = zhuanjia.objects.get(profname=username)
    ll = eval(res.quesnum)
    ll.remove(num)
    if len(ll) == 0:
        zhuanjia.objects.filter(profname=username).update(quesnum='')
    else:
        zhuanjia.objects.filter(profname=username).update(quesnum=ll)
    return HttpResponse('')

def profqnum(req):
    pname = req.GET.get('pname', None)
    result = zhuanjia.objects.filter(profname=pname)
    print(result)
    if result[0].quesnum == '':
        return HttpResponse('')
    else:
        js = eval(result[0].quesnum)
        jsd = []
        for i in js:
            res = luntan.objects.get(id=i)
            jsd.append({'num':res.id,'tit':res.title})
        jsobj = {'qn': jsd}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)

def receti(req):
    title = req.POST.get('title')
    content = req.POST.get('content')
    username = req.POST.get('username')
    profs = req.POST.get('profs')
    try:
        res = luntan.objects.get(title=title)
        return HttpResponse('havegot')
    except :
        pass
    test1 = luntan(title=title,content=content,username=username)
    test1.save()
    rest = luntan.objects.filter(title=title)

    if ',' not in profs:
        p = profs
        result = zhuanjia.objects.filter(profname=p)
        if result[0].quesnum == '':
            zhuanjia.objects.filter(profname=p).update(quesnum=[rest[0].id])
        else:
            pnum = eval(result.quesnum)
            pnum.append(rest.id)
            zhuanjia.objects.filter(profname=p).update(quesnum=pnum)
    else:
        
        p = profs.split(',')
        for i in p:
            result = zhuanjia.objects.filter(profname=i)
            print(result)
            if result[0].quesnum == '':
                zhuanjia.objects.filter(profname=i).update(quesnum=[rest[0].id])
            else:
                pnum = eval(result[0].quesnum)
                pnum.append(rest[0].id)
                zhuanjia.objects.filter(profname=i).update(quesnum=pnum)

    return HttpResponse('ok')

def huifuread(req):
    num = req.GET.get('num')
    res = luntan.objects.get(id=num)
    if res.comment != '':
        js = eval(res.comment)
        jsobj = {'comment': js}
        jsdata = json.dumps(jsobj)
        return HttpResponse(jsdata)
    else:
        return HttpResponse('')


def recehuifu(req):
    username = req.POST.get('username')
    comm = req.POST.get('comm')
    id = req.POST.get('id')
    res = luntan.objects.get(id=id)
    if res.comment == '':

        conlist = [{'username':username,'comm':comm}]
        res.comment = conlist
        res.save()
    else:

        ud = eval(res.comment)
        ud.append({'username':username,'comm':comm})
        res.comment = ud
        res.save()
    return HttpResponse('ok')

def luntandata(req):
    page = int(req.GET.get('page', None))
    n = 15  #每页显示的数量
    list = luntan.objects.order_by('-id')[n*(page-1):n*(page-1)+n]
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

def ltread(req):
    num = req.GET.get('num')
    res = luntan.objects.get(id=num)
    jsobj = {'title':res.title,'content':res.content,'username':res.username}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)