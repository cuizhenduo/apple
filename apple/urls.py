"""apple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from art.views import test,readnews,downapk
from tech.views import zsdata,zsread,zhongshudata,zhongshuread,wsdata,wsread
from buildy.views import buildyread,buildydata
from earthandwater.views import earthdata,earthread,shifeidata,shifeiread,waterdata,waterread
from jian.views import winjiandata,winjianread,sumjiandata,sumjianread
from har.views import blotimedata,blotimeread,tiedata,tieread,untiedata,untieread,collectdata,collectread
from hapast.views import chongdata,chongread,bingdata,bingread,caodata,caoread
from machine.views import machinedata,machineread
from other.views import otherdata,otherread
from userinfo.views import getuser,login,sea
from prof.views import proflogin,showprof
from luntan.views import receti,luntandata,ltread,recehuifu,huifuread,profqnum,setpnum
from django.views.static import serve
from .upload import upload_image
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^test/$',test),
    url(r'^downapk/$',downapk),
    url(r'^readnews/$',readnews),
    url(r'^zsdata/$',zsdata),
    url(r'^zsread/$',zsread),
    url(r'^zhongshudata/$',zhongshudata),
    url(r'^zhongshuread/$',zhongshuread),
    url(r'^wsdata/$',wsdata),
    url(r'^wsread/$',wsread),
    url(r'^buildydata/$',buildydata),
    url(r'^buildyread/$',buildyread),
    url(r'^earthdata/$',earthdata),
    url(r'^earthread/$',earthread),
    url(r'^shifeidata/$',shifeidata),
    url(r'^shifeiread/$',shifeiread),
    url(r'^waterdata/$',waterdata),
    url(r'^waterread/$',waterread),
    url(r'^winjiandata/$', winjiandata),
    url(r'^winjianread/$', winjianread),
    url(r'^sumjiandata/$', sumjiandata),
    url(r'^sumjianread/$', sumjianread),
    url(r'^blotimedata/$', blotimedata),
    url(r'^blotimeread/$', blotimeread),
    url(r'^tiedata/$', tiedata),
    url(r'^tieread/$', tieread),
    url(r'^untiedata/$', untiedata),
    url(r'^untieread/$', untieread),
    url(r'^collectdata/$', collectdata),
    url(r'^collectread/$', collectread),
    url(r'^chongdata/$', chongdata),
    url(r'^chongread/$', chongread),
    url(r'^bingdata/$', bingdata),
    url(r'^bingread/$', bingread),
    url(r'^caodata/$', caodata),
    url(r'^caoread/$', caoread),
    url(r'^machinedata/$', machinedata),
    url(r'^machineread/$', machineread),
    url(r'^otherdata/$', otherdata),
    url(r'^otherread/$', otherread),
    url(r'^getuser/$', getuser),
    url(r'^login/$', login),
    url(r'^proflogin/$', proflogin),
    url(r'^receti/$', receti),
    url(r'^luntandata/$', luntandata),
    url(r'^ltread/$', ltread),
    url(r'^recehuifu/$', recehuifu),
    url(r'^huifuread/$', huifuread),
    url(r'^sea/$', sea),
    url(r'^showprof/$', showprof),
    url(r'^profqnum/$', profqnum),
    url(r'^setpnum/$', setpnum),

]
