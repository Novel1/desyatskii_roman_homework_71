# Generated by Django 4.2 on 2023-04-19 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accounts_options_alter_accounts_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='gender',
            field=models.CharField(blank=True, choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина'), ('Другое', 'Другое')], max_length=30, null=True),
        ),
    ]
