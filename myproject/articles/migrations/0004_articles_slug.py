# Generated by Django 5.1.3 on 2024-11-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_user_articles_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
