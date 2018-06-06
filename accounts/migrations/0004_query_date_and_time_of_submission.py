# Generated by Django 2.0.6 on 2018-06-06 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_query_moderation_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='date_and_time_of_submission',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
