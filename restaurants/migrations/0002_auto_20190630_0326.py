# Generated by Django 2.2.2 on 2019-06-30 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='state',
            field=models.CharField(default='this is empty', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='url',
            field=models.CharField(default='no.url', max_length=10000),
            preserve_default=False,
        ),
    ]
