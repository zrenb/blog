from datetime import datetime
from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True, verbose_name="分类ID")
    cat_name = models.CharField(max_length=50, verbose_name="分类名称")
    parent = models.IntegerField(default=0, verbose_name="父分类ID")
    # parent = models.IntegerField('self', on_delete=models.CASCADE, verbose_name="父类", default=0)
    is_show = models.IntegerField(choices=((1, "是"), (0, "否")), default=0, verbose_name="是否显示")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        unique_together = ('cat_name',)
        db_table = "zjm_category"
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cat_name


class Article(models.Model):
    ar_id = models.AutoField(primary_key=True, verbose_name="文章ID")
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name="文章分类")
    title = models.CharField(max_length=100, verbose_name="文章标题")
    content = UEditorField(verbose_name=u"文章类容", width=600, height=300, imagePath="articles/mued/",
                           filePath="articles/fued/", default='')
    intro = models.TextField(default='', verbose_name="简单描述")
    is_show = models.IntegerField(choices=((1, u"是"), (0, u"否")), default=0, verbose_name=u"是否前端显示")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    r_number = models.IntegerField(default=0, verbose_name="阅读数")

    class Meta:
        db_table = "zjm_article"
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
