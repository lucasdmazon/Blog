# Generated by Django 4.0.6 on 2023-05-17 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
