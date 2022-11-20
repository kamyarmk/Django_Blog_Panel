# Generated by Django 4.1.1 on 2022-11-03 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment_post_remove_posts_ownerid_delete_comments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Slug', models.CharField(max_length=100)),
                ('Parent', models.CharField(default=0, max_length=25)),
                ('Date', models.DateField(default=datetime.datetime(2022, 11, 3, 20, 28, 28, 284786, tzinfo=datetime.timezone.utc))),
                ('Meta_Keyword', models.CharField(max_length=50)),
                ('Meta_Desc', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Slug', models.CharField(max_length=100)),
                ('Date', models.DateField(default=datetime.datetime(2022, 11, 3, 20, 28, 28, 285594, tzinfo=datetime.timezone.utc))),
                ('Meta_Keyword', models.CharField(max_length=50)),
                ('Meta_Desc', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='OwnerId',
            new_name='Author',
        ),
        migrations.AddField(
            model_name='post',
            name='Meta_Desc',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Meta_Keyword',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='Slug',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 11, 3, 20, 28, 28, 286047, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.ManyToManyField(to='posts.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='Tags',
            field=models.ManyToManyField(to='posts.tag'),
        ),
    ]