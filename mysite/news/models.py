from django.contrib.admin import filters
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')      #   атрибут "blank=True" -> поле необязательное для заполнения. Атрибут необязательный
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')   #   атрибут "auto_now_add=True" создает дату и впемя только раз. При обновлении записи, время не поменяется
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')         #   дата и время обновляются при корректировке новости
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True) #   разбивает загружаемые изображения по папкам и датам (каждый день)
    sign_of_publication = models.BooleanField(default=True, verbose_name='Признак публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')  #   Новость защищена от удаления
                                                    #   если таблица "Категория" создана ПОСЛЕ таб."News", указывать на до в ковычках
                                                    #   в противном случае, просто ссылаемся на таблицу
                                                    #   category = models.ForeignKey('Category')        #       если таблица "Категория" создана ПОСЛЕ таб."News", указывать надо в ковычках
                                                    #   в противном случае, просто ссылаемся на таблицу: category = models.ForeignKey(Category)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def my_func(self):
        return 'Hello from model'

    def __str__(self):
        return self.title

    # def get_size_used(self):
    #     return filters.filesizeformat(self.bytes)

    class Meta:
        verbose_name = 'Новость'            #   при редактировании новости вверху отображается "изменить НОВОСТЬ"
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):                                     #  монтирует кнопку в админке в "категории" (внутри) "смотреть на сайте"
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'            #   при редактировании новости вверху отображается "изменить НОВОСТЬ"
        verbose_name_plural = 'Категории'
        ordering = ['title']

# class User(AbstractUser):
#     pass