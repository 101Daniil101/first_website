from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('users/<str:name_user>/', views.account, name='account'),
    path('articles/create/', views.create_article), 
    path('articles/<str:art_slug>/redact/', views.redact_article, name='redact_article'),
    path('articles/<str:art_slug>/delete/', views.delete_article, name='delete_article'),
    path('articles/<str:art_slug>/', views.view_article, name='view_article'), #Не совсем понял, как делать крутые слаги, поэтому просто в маршруте указываю тип строка
    path('flow/<str:cat_slug>/articles', views.show_category, name='category'),
]