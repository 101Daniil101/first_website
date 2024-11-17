from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import forms
from . import models

def create_article(request):
    print(request.user.username)
    if request.method == 'POST':
        form = forms.AddPost(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                article = models.Articles.objects.create(title=cd['title'], content=['content'])
                article.author = request.user
                article.save()
                print("Успешно")
            except:
                print("Ошибка")
                form.add_error(None, 'Ошибка добавления публикации')
            return HttpResponseRedirect(reverse('home'))
    else:
        form = forms.AddPost()
    return render(request, 'articles/create_article.html', {'form': form})

def account(request, name_user):
    print(request.user)
    return render(request, 'articles/account.html')

def main_page(request):
    return render(request, 'articles/main_page.html')