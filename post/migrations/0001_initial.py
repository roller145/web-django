# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 11:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('sign', models.CharField(max_length=31, verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u044c')),
                ('picture', models.ImageField(upload_to=b'', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u0430')),
                ('is_published', models.BooleanField(default=False, verbose_name='\u0411\u044b\u043b\u043e \u043b\u0438 \u043e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('last_changes', models.DateTimeField(auto_now=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
                ('gallery', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery', verbose_name='\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u043a \u0433\u0430\u043b\u0435\u0440\u0435\u0435')),
            ],
            options={
                'ordering': ('-created_at',),
                'verbose_name': '\u0422\u0432\u043e\u0440\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0422\u0432\u043e\u0440\u0435\u043d\u0438\u044f',
            },
        ),
    ]
