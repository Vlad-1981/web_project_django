from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category

# -----   АВТОРИЗАЦИЯ ----------
from .forms import NewsForm, UserLoginForm, UserRegisterForm        #   RegisterUserForm,
from django.contrib.auth import login, logout
# ----------------------------------------------------------------

from .utils import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class HomeNews(ListView):                                       #   домашняя страница
                                                                #   к классу привязывается базовый шаблон "news_list"
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная страница'}                       #   используется для статичных данных
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):          #   используется для динамичных данных
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(sign_of_publication=True).select_related('category')             #   получаем новости на сайте ТОЛЬКО с признаком публикации == True


class NewsFromCategory(ListView):                               #   просмотр новостей по категориям
    model = News
    # template_name = 'news/home_news_list.html'
    template_name = 'news/home_news_list.html'                  #   поскольку шаблон "home_news_list.html" идентичен "category", оставляем его в качестве базового
    context_object_name = 'news'
    allow_empty = False                                         #   Предовращает ошибку при выборе несуществующей категории (запрет на показ пустых списков)
                                                                #   аналогично и для рубрик с пустыми новостями
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):            #   используется для динамичных данных
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])      #   в title передается название категории
        return context

    def get_queryset(self):
        return News.objects.filter(
                                    category_id=self.kwargs['category_id'],
                                    sign_of_publication=True).select_related('category')              #   получаем новости на сайте ТОЛЬКО с признаком публикации == True


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # template_name = 'news/news_detail.html'               #   переадет по умолчанию
    # pk_url_kwarg = 'news_id'


class CreateNews(LoginRequiredMixin, CreateView):       #   "LoginRequiredMixin" добавление новости только для авторизованных
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')          #   после добавления новости, переходим на главную страницу

    login_url = '/admin/'       #   при попытке добавить новость на сайте, переход к авторизации в админке
    # raise_exception = True          #   при попытке добавить новость на сайте, выбрасывает ошибку "403 Forbidden"



def register(request):                                          #   регистрация пользователя
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'title': 'Registration', 'form': form})
# ----------------------------------------------------------------------------------------------------------

def user_login(request):                                        #   авторизация пользователя
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'title': 'Login', 'form': form})


def user_logout(request):                                        #   выход из системы
    logout(request)
    return redirect('login')


# ------------------------------------------------------------------------------------------------------------------------------
# Использовали класс "class HomeNews(ListView):"
# ---------------------------------------------------
# def index(request):
#     news = News.objects.all()
#     # categories = Category.objects.all()
#     context = {
#                 'list_news': news,
#                 'title': 'Список новостей',
#                 # 'categories': categories,
#     }
#
#     return render(request=request, template_name='news/index.html', context=context)              #   render принимает 3 параметра


# ------------------------------------------------------------------------------------------------------------------------------
# Использовали класс "class NewsFromCategory(ListView):"
# ---------------------------------------------------
# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)                 #   "category_id" - поле в БД -> таблица "News"
#     # categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html',
#                                                     {
#                                                         'title': 'Категории',
#                                                         'list_news': news,
#                                                         # 'categories': categories,
#                                                         'category': category
#                                                     })
# ------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------
# Использовали класс "class ViewNews(DetailView):"
# ---------------------------------------------------
# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item})
# ------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------------
# Использовали класс "class CreateNews(CreateView):"
# ---------------------------------------------------
# def add_news(request):                          #       добавляет новость       #   http://127.0.0.1:8000/add_news
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)           #   перенаправляет на вновь созданную новость
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'title': 'Добавить статью', 'form': form},)
# ------------------------------------------------------------------------------------------------------------------------------


# def login(request):
#     if request.method == 'POST':
#         pass
#         # login_form = LoginForm(data=request.POST)
#         # if login_form.is_valid():
#         #     pass
#         #     # do something when valid
#     else:
#         login_form = LoginForm()
#     return render(request, 'login.html', {'login_form': login_form})


def test(request):
    objects = [f"Новость_{str(i)}" for i in range(1, 10)]
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)                             #   метод "get_page": если новости закончились и мы пытаемся перейти на след. страницу, не выдает ошибку
    return render(request, 'news/test.html', {'page_obj': page_objects})


