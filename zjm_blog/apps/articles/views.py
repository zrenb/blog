from pprint import pprint

from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Article


class IndexView(View):
    def get(self, request):
        """
        文章分类数据
        文章数据
        :param request:
        :return:
        """
        categorys = Category.objects.all().filter(parent=0, is_show=1)
        python_cats = Category.objects.filter(parent__exact=1)
        articles = Article.objects.all().values('ar_id', 'title', 'cat_id', 'intro', 'create_time',
                                                'cat_id__cat_name').filter(is_show=1).order_by('-ar_id')[0:10]
        return render(request, 'articles/index.html', {
            'categorys': categorys,
            'articles': articles,
            'python_cats': python_cats
        })


class Articles(View):
    def get(self, request, a_id):

        try:
            article = Article.objects.get(ar_id=int(a_id))
        except:
            return HttpResponseRedirect(reverse("index"))
        article.r_number = article.r_number + 1
        article.save()
        # 相关文章
        relevant_article = Article.objects.filter(cat_id=article.cat_id).exclude(ar_id=int(a_id)).order_by('-r_number')[
                           0:10]
        # 上一篇文章
        try:
            up_article = Article.objects.get(ar_id=int(a_id) - 1)
        except:
            up_article = False
        # 下一篇文章
        try:
            next_article = Article.objects.get(ar_id=int(a_id) + 1)
        except:
            next_article = False
        # if article:
        #     return HttpResponse("你来晚了哦！文章已经不存在了")
        categorys = Category.objects.all().filter(parent=0, is_show=1)
        return render(request, 'articles/info.html', {
            "article": article,
            'categorys': categorys,
            'relevant_article': relevant_article,
            'up_article': up_article,
            'next_article': next_article
        })


class CatArticlesList(View):
    def get(self, request, cat_id):
        articles = Article.objects.values('ar_id', 'title', 'cat_id', 'intro', 'create_time',
                                          'cat_id__cat_name').filter(
            cat_id=int(cat_id))
        category = Category.objects.get(cat_id=int(cat_id))
        categorys = Category.objects.all().filter(parent=0, is_show=1)
        python_cats = Category.objects.filter(parent__exact=1)
        return render(request, 'articles/list.html', {
            'articles': articles,
            'category': category,
            'categorys': categorys,
            'python_cats': python_cats
        })


class AboutMe(View):
    def get(self, request):
        categorys = Category.objects.all().filter(parent=0, is_show=1)
        python_cats = Category.objects.filter(parent__exact=1)
        return render(request, 'articles/about.html', {
            'categorys': categorys,
            'python_cats': python_cats
        })
