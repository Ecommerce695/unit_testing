# Generated by Django 4.2.5 on 2023-09-21 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_alter_account_activation_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnoxAuthtoken',
            fields=[
                ('digest', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('expiry', models.DateTimeField(blank=True, null=True)),
                ('token_key', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'knox_authtoken',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='account_activation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 21, 14, 34, 41, 824641)),
        ),
        migrations.AlterField(
            model_name='account_activation',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 23, 14, 34, 41, 824641)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 21, 14, 34, 41, 819699)),
        ),
    ]
