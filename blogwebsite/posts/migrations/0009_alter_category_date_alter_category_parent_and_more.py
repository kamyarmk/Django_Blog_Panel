# Generated by Django 4.1.1 on 2022-11-09 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_category_date_alter_post_date_alter_tag_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 9, 17, 28, 24, 937245, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='Parent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 9, 17, 28, 24, 938888, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 9, 17, 28, 24, 938215, tzinfo=datetime.timezone.utc)),
        ),
    ]
