# Generated by Django 2.2.24 on 2021-09-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baadalbeats', '0005_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20000000)),
                ('music', models.CharField(default='', max_length=20000000)),
            ],
        ),
    ]
