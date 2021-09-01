# Generated by Django 2.2.24 on 2021-08-31 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baadalbeats', '0004_watchlater'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('music_id', models.CharField(default='', max_length=20000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
