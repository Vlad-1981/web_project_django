from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'update_at', 'sign_of_publication')    #   добавляет поля таблицы
    list_display_links = ('id', 'title')                                                #   делает колонки таблицы ссылками (для их открытия)
    search_fields = ('title', 'content')                                                #   поиск по полям: 'title' и 'content'
    list_editable = ('sign_of_publication',)       #   поскольку это кортеж, ставим запятую. Поле является редактируемым
    list_filter = ('sign_of_publication', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)                      #   поскольку это кортеж, ставим запятую




admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)







