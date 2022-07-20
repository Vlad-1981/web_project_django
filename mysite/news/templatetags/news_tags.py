from django import template
from django.db.models import Count, F
from news.models import Category

register = template.Library()

@register.simple_tag(name='get_list_categories')                      #   в скобках можно присвоить другое имя функции "get_categories"
def get_categories():
    return Category.objects.all()

# ---------------------------------------------------
# Формирует "sidebar" с аргументами
# ----------------------
# @register.inclusion_tag('news/list_categories.html')
# def show_categories(arg1='Hello', arg2='World'):
#     categories = Category.objects.all()
#     # categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
#     # categories = Category.objects.annotate(cnt=Count('news', filter=F('news__sign_of_publication'))).filter(cnt__gt=0)
#     return {'categories': categories, 'arg1': arg1, 'arg2': arg2}          #   передаем ключ словаря "categories" в шаблон "list_categories"


# ---------------------------------------------------
# Формирует "sidebar"
# ----------------------
@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__sign_of_publication'))).filter(cnt__gt=0)
    return {'categories': categories}          #   передаем ключ словаря "categories" в шаблон "list_categories"
