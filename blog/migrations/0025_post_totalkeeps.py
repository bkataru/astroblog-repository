# Generated by Django 2.0.6 on 2018-06-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20180606_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='totalkeeps',
            field=models.IntegerField(default=1),
        ),
    ]
