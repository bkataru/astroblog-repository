# Generated by Django 2.0.6 on 2018-06-06 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_post_totalkeeps'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date_and_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
