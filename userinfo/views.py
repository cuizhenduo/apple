from django.shortcuts import render
from .models import userinfo
import re,json
from django.http import HttpResponse
from art.models import wenzhang
from buildy.models import BuildY
from earthandwater.models import Earth,Shifei,Water
from hapast.models import Chong,Bing,Cao
from har.models import BloTime,Tie,UnTie,Collect
from jian.models import Winjian
from machine.models import Machine
from other.models import Other
from tech.models import KindofEarly,KindofMid,KindofLate
from luntan.models import luntan
from prof.models import zhuanjia
# Create your views here.

def sea(req):
    kwd = req.POST.get('kwd')
    response = []
    list = luntan.objects.all()
    for var in list:
        response.append(str(var.id) + '问答-' + var.title)
    list = wenzhang.objects.all()
    for var in list:
        response.append(str(var.id)+'新闻-'+var.title)
    list = BuildY.objects.all()
    for var in list:
        response.append(str(var.id)+'建园-'+var.title)
    list = Earth.objects.all()
    for var in list:
        response.append(str(var.id)+'土壤-'+var.title)
    list = Shifei.objects.all()
    for var in list:
        response.append(str(var.id)+'施肥-'+var.title)
    list = Water.objects.all()
    for var in list:
        response.append(str(var.id)+'灌水-'+var.title)
    list = Chong.objects.all()
    for var in list:
        response.append(str(var.id)+'虫害-'+var.title)
    list = Bing.objects.all()
    for var in list:
        response.append(str(var.id)+'病害-'+var.title)
    list = Cao.objects.all()
    for var in list:
        response.append(str(var.id)+'草害-'+var.title)
    list = BloTime.objects.all()
    for var in list:
        response.append(str(var.id)+'花期-'+var.title)
    list = Tie.objects.all()
    for var in list:
        response.append(str(var.id)+'套袋-'+var.title)
    list = UnTie.objects.all()
    for var in list:
        response.append(str(var.id)+'解袋-'+var.title)
    list = Collect.objects.all()
    for var in list:
        response.append(str(var.id)+'采收-'+var.title)
    list = Winjian.objects.all()
    for var in list:
        response.append(str(var.id)+'冬剪-'+var.title)
    list = Sumjian.objects.all()
    for var in list:
        response.append(str(var.id)+'夏剪-'+var.title)
    list = Machine.objects.all()
    for var in list:
        response.append(str(var.id)+'机械操作-'+var.title)
    list = Other.objects.all()
    for var in list:
        response.append(str(var.id)+'其他-'+var.title)
    list = KindofEarly.objects.all()
    for var in list:
        response.append(str(var.id)+'早熟-'+var.title)
    list = KindofMid.objects.all()
    for var in list:
        response.append(str(var.id)+'中熟-'+var.title)
    list = KindofLate.objects.all()
    for var in list:
        response.append(str(var.id)+'晚熟-'+var.title)
    print(response)

    suggestions = []
    pattern = '.*'.join(kwd)  # Converts 'djm' to 'd.*j.*m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in response:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append(item)
    jsobj = {'seares': suggestions}
    jsdata = json.dumps(jsobj)
    return HttpResponse(jsdata)

def getuser(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    response = []
    list = userinfo.objects.all()
    for var in list:
        response.append(var.username)
    list = zhuanjia.objects.all()
    for var in list:
        response.append(var.profname)
    if username in response:
        return HttpResponse('had')
    else:
        test1 = userinfo(username=username,password=password)
        test1.save()
        return HttpResponse('ok')

def login(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    try:
        res = userinfo.objects.get(username=username)
    except :
        return HttpResponse('nouser')

    pwd = res.password
    if password == pwd:
        return HttpResponse('ok')
    else:
        return HttpResponse('noeq')