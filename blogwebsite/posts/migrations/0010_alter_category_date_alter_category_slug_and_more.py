# Generated by Django 4.1.2 on 2022-11-10 00:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_category_date_alter_category_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 10, 0, 10, 25, 730449, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='Slug',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 10, 0, 10, 25, 731764, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='Slug',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 10, 0, 10, 25, 731317, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='Slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
