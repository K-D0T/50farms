# Generated by Django 3.1.7 on 2021-03-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210316_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitmodel',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
