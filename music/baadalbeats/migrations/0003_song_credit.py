# Generated by Django 2.2.24 on 2021-08-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baadalbeats', '0002_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='credit',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
