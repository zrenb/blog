# _*_coding:utf-8_*_
"""
+-----------------------------------------------------------------------------------------------------------

@Auth |     'Toss'

@Data |     '2019-03-12 16:01'

+-----------------------------------------------------------------------------------------------------------

"""
from django.conf.urls import url, include
from .views import Articles, CatArticlesList

urlpatterns = [
    url(r'article/(?P<a_id>\d+)', Articles.as_view(), name='info'),
    url(r'category/(?P<cat_id>\d+)', CatArticlesList.as_view(), name='list')
]
