from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('users/<str:name_user>/', views.account, name='account'),
    path('create/', views.create_article), 
]