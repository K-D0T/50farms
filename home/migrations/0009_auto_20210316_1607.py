# Generated by Django 3.1.7 on 2021-03-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210316_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitmodel',
            name='pic',
            field=models.ImageField(upload_to='media_cdn'),
        ),
    ]
