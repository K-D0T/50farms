# Generated by Django 3.1.7 on 2021-03-18 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210317_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitmodel',
            name='dam',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submitmodel',
            name='sire',
            field=models.IntegerField(default=0),
        ),
    ]