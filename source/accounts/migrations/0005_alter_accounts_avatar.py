# Generated by Django 4.2 on 2023-04-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_accounts_comments_post_accounts_liked_posts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='avatar',
            field=models.ImageField(blank=True, default='1.jpeg', null=True, upload_to='uploads/', verbose_name='Аватар'),
        ),
    ]
