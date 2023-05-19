from django.conf import settings
from django.db import models
from django.utils.timezone import now

from blog.models import Article


# Create your models here.

class Comment(models.Model):
    body = models.TextField('正文', max_length=300)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)
    author = models.CharField(verbose_name='评论者', max_length=1, blank=False, default='路人甲')
    article = models.ForeignKey(
        Article,
        verbose_name='文章',
        on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self',
        verbose_name="上级评论",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    is_enable = models.BooleanField(
        '是否显示', default=False, blank=False, null=False)

    class Meta:
        ordering = ['-id']
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def __str__(self):
        return self.body