# Generated by Django 4.0.6 on 2023-05-09 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_data_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 10, 14, 6, 128766, tzinfo=utc)),
        ),
    ]
