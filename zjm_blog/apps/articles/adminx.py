# _*_coding:utf-8_*_
"""
+-----------------------------------------------------------------------------------------------------------

@Auth |     'Toss'

@Data |     '2019-03-12 16:01'

+-----------------------------------------------------------------------------------------------------------

"""
import xadmin
from xadmin import views
from .models import Category,Article


# 全站配置
class BaseSetting(object):
    enable_themes = True  # 主题功能  默认是关闭的
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "诗妤小店"  ### 标题信息
    site_footer = "诗妤小店"  ### 底部信息
    menu_style = "accordion"  ### 菜单栏折叠效果


class ArticleAdmin(object):
    list_display = ['ar_id', 'title', 'cat_id', 'is_show', 'r_number']
    search_fields = ['title']
    list_filter = ['ar_id', 'title', 'cat_id', 'is_show', 'r_number']
    # ordering = ['-click_nums']  ###自定义排序
    # readonly_fields = ['click_nums']  ###定义字段只读
    # exclude = ['fav_nums']  ###自定义不显示列表  readonly_fields和exclude字段不能同时使用
    # list_editable = ['degree', 'name']
    refresh_times = [3, 10]  ###自定义刷新时间
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'
    # inlines = [LessonInline, CourseResourceInline]  ###自定定义章节及课程资源添加操作
    style_fields = {"content": "ueditor"}
    # import_excel = True


class CategoryAdmin(object):
    list_display = ['cat_id', 'cat_name', 'create_time']
    search_fields = ['cat_name']
    list_filter = ['cat_id', 'cat_name', 'create_time']


xadmin.site.register(Article, ArticleAdmin)  # 文章
xadmin.site.register(Category, CategoryAdmin)  # 文章分类
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
