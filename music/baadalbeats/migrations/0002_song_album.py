# Generated by Django 2.2.24 on 2021-08-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baadalbeats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default='', max_length=2000),
        ),
    ]