# Generated by Django 2.2.3 on 2019-07-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20190703_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image_url',
            field=models.URLField(default='http://s3-media2.fl.yelpcdn.com/bphoto/MmgtASP3l_t4tPCL1iAsCg/o.jpg', max_length=10000),
            preserve_default=False,
        ),
    ]