from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('articles.urls')),
]

#Добавь страницу not_found
#Попробуй добавить лайки
#Сделай виджеты для полей
#Попробуй сохранить файл БД и отправить ему
