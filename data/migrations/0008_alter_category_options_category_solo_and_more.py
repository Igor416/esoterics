# Generated by Django 5.0.1 on 2024-11-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_delete_brand_alter_prevlife_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['solo', 'order'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='solo',
            field=models.BooleanField(default=True, verbose_name='Одиночная матрциа'),
        ),
        migrations.AlterField(
            model_name='blocktype',
            name='positions',
            field=models.CharField(blank=True, max_length=35, verbose_name='Позиции'),
        ),
    ]
