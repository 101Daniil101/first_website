from django.db import models
from django.contrib.auth import get_user_model 

class Articles(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, default='')
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=True) #Не понял, как работает функция get_user_model()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.CharField(max_length=255, unique=True, db_index=True)

    #Создай категории!!