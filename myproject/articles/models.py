from django.db import models
from django.contrib.auth import get_user_model 

class Articles(models.Model):
    title = models.CharField()
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True) #Апдейт не работает
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, null=True) #Не понял, как работает функция get_user_model()