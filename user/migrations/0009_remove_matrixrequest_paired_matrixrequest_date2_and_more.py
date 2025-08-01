# Generated by Django 5.0.1 on 2024-11-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_matrixrequest_paired_alter_matrixrequest_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matrixrequest',
            name='paired',
        ),
        migrations.AddField(
            model_name='matrixrequest',
            name='date2',
            field=models.CharField(blank=True, max_length=10, verbose_name='Дата рождения 2'),
        ),
        migrations.AddField(
            model_name='matrixrequest',
            name='name2',
            field=models.CharField(blank=True, max_length=32, verbose_name='Имя 2'),
        ),
        migrations.AlterField(
            model_name='matrixrequest',
            name='gender',
            field=models.CharField(choices=[('m', 'парень'), ('f', 'девушка'), ('c', 'совместимость')], max_length=1, verbose_name='Гендер'),
        ),
    ]
