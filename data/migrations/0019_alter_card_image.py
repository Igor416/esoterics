# Generated by Django 5.0.1 on 2024-12-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.CharField(blank=True, default='', max_length=8, unique=True, verbose_name='Картинка'),
        ),
    ]
