from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255) #поле переменной длины до 255 символов
    content = models.TextField(blank=True) #blank=True данное поле допускается не заполнять
    created_at = models.DateTimeField(auto_now_add=True) #дата сохранения записи
    photo = models.ImageField(upload_to='photos/%Y/%m/%d') #создаст поле для загрузки изображения

    #чтобы печаталось название статьи
    def __str__(self):
        return  self.title