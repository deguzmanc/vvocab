# Generated by Django 5.0.6 on 2024-06-11 23:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('url', models.URLField(validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Enter a valid youtube URL.', regex='(?:https?://)?(?:www\\.)?(?:youtube\\.com/watch\\?v=|youtu\\.be/)([a-zA-Z0-9_-]{11})')])),
            ],
        ),
    ]
