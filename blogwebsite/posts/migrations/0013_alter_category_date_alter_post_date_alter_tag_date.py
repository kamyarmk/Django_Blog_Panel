# Generated by Django 4.1.1 on 2022-11-20 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_category_date_alter_post_date_alter_tag_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 20, 3, 52, 18, 954601, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 20, 3, 52, 18, 955779, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 20, 3, 52, 18, 955351, tzinfo=datetime.timezone.utc)),
        ),
    ]