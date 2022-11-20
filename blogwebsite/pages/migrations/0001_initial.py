# Generated by Django 4.1.2 on 2022-11-01 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Date', models.DateField()),
                ('Status', models.CharField(choices=[('P', 'Published'), ('H', 'Hidden'), ('D', 'Deleted')], max_length=1)),
                ('Content', models.CharField(max_length=250)),
                ('OwnerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]