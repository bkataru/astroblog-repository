# Generated by Django 2.0.6 on 2018-06-06 02:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20180606_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='starredby',
            field=models.ManyToManyField(related_name='starred_by_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
