# Generated by Django 4.2.5 on 2023-09-25 05:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_alter_account_activation_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_activation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 25, 10, 45, 36, 431111)),
        ),
        migrations.AlterField(
            model_name='account_activation',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 27, 10, 45, 36, 431111)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 25, 10, 45, 36, 426119)),
        ),
    ]
