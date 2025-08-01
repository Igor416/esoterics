# Generated by Django 5.0.1 on 2024-11-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_sexiness_alter_block_options_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.AlterModelOptions(
            name='prevlife',
            options={'ordering': ['code'], 'verbose_name': 'Предедущая жизнь', 'verbose_name_plural': 'Предедущие жизни'},
        ),
        migrations.AlterField(
            model_name='prevlife',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='program',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='sexiness',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Код'),
        ),
    ]
