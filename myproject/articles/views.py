from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import forms
from . import models
from django.contrib.auth import get_user_model



def create_article(request):
    if request.method == 'POST':
        form = forms.AddPost(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                #Я изначально создал категории в БД, поэтому если название прописать неправильно, то объект не создастся, думаю вполне логично
                cat = models.Category.objects.get(title=cd['cat'])
                article = models.Articles.objects.create(title=cd['title'], content=cd['content'])
                article.author = request.user
                article.slug = str(request.user) + '-' + '+'.join(str(article.title).split())
                article.cat_id = cat.id
            except:
                return render(request, 'articles/create_article.html', {'form': form})
            article.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = forms.AddPost()
    return render(request, 'articles/create_article.html', {'form': form})


def account(request, name_user):
    User = get_user_model()

    try:
        author = request.user.id
    except:
        author = -1
    try:
        author_id = User.objects.get(username=name_user).id
        articles = models.Articles.objects.filter(author=author_id)
    except:
        name_user = f"Пользователь {name_user} не зарегестрирован"
        articles = ""

    return render(request, 'articles/account.html', {'author_id': author, 'articles': articles, 'name_user': name_user})


def main_page(request):
    User = get_user_model()

    try:
        id_user = request.user.id
        articles = models.Articles.objects.exclude(author=id_user)
    except:
        articles = "Статей пока что нет"

    return render(request, 'articles/main_page.html', {'articles': articles})


def view_article(request, art_slug):
    try:
        article = models.Articles.objects.get(slug=art_slug)
    except:
        article = 'Такой статьи нет'
    
    return render(request, 'articles/article.html', {'article': article})


def redact_article(request, art_slug):
    article = models.Articles.objects.get(slug=art_slug) #Возможно, здесь ошибка вылезет, если статей не будет

    try:
        user_id = request.user.id
    except:
        user_id = -1

    if user_id == article.author.id:
        if request.method == 'POST':
            form = forms.AddPost(request.POST)
            if form.is_valid():

                cd = form.cleaned_data
                try:
                    #Я изначально создал категории в БД, поэтому если название прописать неправильно, то объект не создастся, думаю вполне логично
                    cat = models.Category.objects.get(title=cd['cat'])
                    article.title = cd['title']
                    article.content = cd['content']
                    article.slug = str(request.user) + '-' + '+'.join(str(article.title).split())
                    article.cat_id = cat.id
                except:
                    return render(request, 'articles/redact_article.html', {'form': form, 'title': article.title})
                article.save()
                return HttpResponseRedirect(reverse('account', args=(f'{request.user.username}', )))
        else:
            form = forms.AddPost()
        return render(request, 'articles/redact_article.html', {'form': form, 'title': article.title})
    else:
        return HttpResponseRedirect(reverse('home'))
    

def delete_article(request, art_slug):
    article = models.Articles.objects.get(slug=art_slug) #Возможно, здесь ошибка вылезет

    try:
        user_id = request.user.id
    except:
        user_id = -1

    if user_id == article.author.id:
        if request.method == 'POST':
            article = models.Articles.objects.get(slug=art_slug)
            article.delete()
            return HttpResponseRedirect(reverse('account', args=(f'{request.user.username}', )))
        return render(request, 'articles/delete_article.html', {'title': article.title})
    else:
        return HttpResponseRedirect(reverse('home'))
    
def show_category(request, cat_slug):
    User = get_user_model()

    try:
        id_user = request.user.id
        articles = models.Articles.objects.filter(cat__slug=cat_slug) & models.Articles.objects.exclude(author=id_user)
    except:
        raise Http404("Page Not Found")
    
    return render(request, 'articles/category.html', {'articles': articles})