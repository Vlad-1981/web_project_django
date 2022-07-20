from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'update_at', 'sign_of_publication', 'get_photo')    #   добавляет поля таблицы
    list_display_links = ('id', 'title')                                                #   делает колонки таблицы ссылками (для их открытия)
    search_fields = ('title', 'content')                                                #   поиск по полям: 'title' и 'content'
    list_editable = ('sign_of_publication',)       #   поскольку это кортеж, ставим запятую. Поле является редактируемым
    list_filter = ('sign_of_publication', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'sign_of_publication', 'created_at', 'update_at')     #   выводит список полей в самой новости

    readonly_fields = ('get_photo', 'created_at', 'update_at')     #   список нередактируемых полей
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')     #   выводит html код картинки
        else:
            return 'Фото отсутствует'


    get_photo.short_description = 'Фото'            #   заменяет title "get_photo" в админке на "фото"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)                      #   поскольку это кортеж, ставим запятую




admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.site_title = 'Панель новостей'                   #   изменяет title админки
admin.site.site_header = 'Панель новостей DJANGO'           #   изменяет header админки




