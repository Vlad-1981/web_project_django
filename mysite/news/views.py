from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category
from forms import NewsForm


def index(request):                                         #   http://127.0.0.1:8000/news
    news = News.objects.all()                               #   сортировка по дате создания в обратном порядке
    # categories = Category.objects.all()
    context = {
                'list_news': news,
                'title': 'Список новостей',
                # 'categories': categories,
    }

    return render(request=request, template_name='news/index.html', context=context)              #   render принимает 3 параметра

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)                 #   "category_id" - поле в БД -> таблица "News"
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html',
                                                    {
                                                        'title': 'Категории',
                                                        'list_news': news,
                                                        # 'categories': categories,
                                                        'category': category
                                                    })

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):                          #       добавляет новость       #   http://127.0.0.1:8000/add_news
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'title': 'Добавить статью', 'form': form},)