# Generated by Django 2.1.7 on 2019-03-12 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaportalapp', '0006_useraccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='social_media_link',
        ),
    ]
