# Generated by Django 2.1.7 on 2022-06-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除标记'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除标记'),
        ),
    ]