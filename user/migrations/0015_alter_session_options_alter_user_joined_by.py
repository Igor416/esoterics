# Generated by Django 5.0.1 on 2024-12-13 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_matrixrequest_options_referrallink_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['-date'], 'verbose_name': 'Сессия', 'verbose_name_plural': 'Сессии'},
        ),
        migrations.AlterField(
            model_name='user',
            name='joined_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referrals', to='user.referrallink', verbose_name='Присоеденился по ссылке'),
        ),
    ]
