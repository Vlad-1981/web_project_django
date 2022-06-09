from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)      #   атрибут "blank=True" -> поле необязательное для заполнения. Атрибут необязательный
    created_at = models.DateTimeField(auto_now_add=True)   #   атрибут "auto_now_add=True" создает дату и впемя только раз. При обновлении записи, время не поменяется
    update_at = models.DateTimeField(auto_now=True)         #   дата и время обновляются при корректировке новости
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/') #   разбивает загружаемые изображения по папкам и датам (каждый день)
    sign_of_publication = models.BooleanField(default=True)

    def __str__(self):
        return self.title