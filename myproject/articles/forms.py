from django import forms

class AddPost(forms.Form):
    title = forms.CharField(label="Название", max_length=200)
    content = forms.CharField(label="Содержимое статьи", widget=forms.Textarea())
    cat = forms.CharField(label="Категория", max_length=200)


