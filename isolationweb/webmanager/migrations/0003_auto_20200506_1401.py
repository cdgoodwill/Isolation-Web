# Generated by Django 3.0.6 on 2020-05-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmanager', '0002_auto_20200506_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=8, max_digits=11),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.DecimalField(decimal_places=8, max_digits=11),
        ),
    ]
