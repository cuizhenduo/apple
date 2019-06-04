from django.db import models

# Create your models here.
class luntan(models.Model):
    title = models.CharField('标题',max_length=200)
    username = models.CharField('用户', max_length=200)
    content = models.TextField('内容')
    comment = models.TextField('评论')
    time = models.DateTimeField('时间', auto_now=True)
    class Meta:
        verbose_name = '论坛'
        verbose_name_plural = '论坛'
    def __unicode__(self):
        return self.title