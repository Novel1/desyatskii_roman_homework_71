# Generated by Django 4.2 on 2023-04-19 12:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
        ('accounts', '0003_alter_accounts_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='comments_post',
            field=models.ManyToManyField(related_name='user_comments', to='posts.post', verbose_name='Прокоментированные публикации'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='liked_posts',
            field=models.ManyToManyField(related_name='user_likes', to='posts.post', verbose_name='Понравившиеся публикации'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]
