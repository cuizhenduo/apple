from django.db import models

# Create your models here.
class zhuanjia(models.Model):
    profname = models.CharField('专家名',max_length=200)
    password = models.CharField('密码', max_length=200)
    quesnum = models.TextField('向我提问的问题标号',blank=True,null=True)
    class Meta:
        verbose_name = '专家信息'
        verbose_name_plural = '专家信息'
    def __unicode__(self):
        return self.title