# Generated by Django 3.0.3 on 2020-03-20 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0004_auto_20200320_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='yr',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 12, 14, 32, 337627)),
        ),
        migrations.AlterField(
            model_name='materials',
            name='img',
            field=models.FileField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='materials',
            name='yr',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 12, 14, 32, 299729)),
        ),
    ]
