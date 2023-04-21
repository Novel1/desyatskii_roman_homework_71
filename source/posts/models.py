from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    descriptions = models.CharField(verbose_name='Описание', null=True, max_length=200)
    image = models.ImageField(verbose_name='Фото', null=False, blank=True, upload_to='posts')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='posts', null=False, blank=False,
                               on_delete=models.CASCADE)
    likes_count = models.IntegerField(verbose_name='Количество лайков', default=0)
    comments_count = models.IntegerField(verbose_name='Количество коментариев', default=0)


class Comment(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='comments', null=False, blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='posts.Post', related_name='comments', null=False,
                             blank=False, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Комментарий', null=False, blank=False, max_length=200)


class Like(models.Model):
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='author_like', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Публикация', to='posts.Post', related_name='post_like', null=False,
                             blank=False, on_delete=models.CASCADE)





