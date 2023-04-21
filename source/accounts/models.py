from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class Accounts(AbstractUser):

    GENDER_CHOICES = [
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
        ('Другое', 'Другое'),
    ]
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True, blank=True)
    inform = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=True
    )
    avatar = models.ImageField(
        default='1.jpeg',
        null=True,
        blank=True,
        upload_to='uploads/',
        verbose_name='Аватар',
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Понравившиеся публикации',
        to='posts.Post',
        related_name='user_likes'
    )
    comments_post = models.ManyToManyField(
        verbose_name='Прокоментированные публикации',
        to='posts.Post',
        related_name='user_comments'
    )
    subscriptions = models.ManyToManyField(
        to='accounts.Accounts',
        symmetrical=False,
        related_name='subscribers',
        verbose_name='Подписки',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


