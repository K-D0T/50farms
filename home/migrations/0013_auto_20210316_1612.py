# Generated by Django 3.1.7 on 2021-03-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210316_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitmodel',
            name='pic',
            field=models.FileField(upload_to='cows/'),
        ),
    ]
