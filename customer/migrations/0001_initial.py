# Generated by Django 4.2.5 on 2023-09-14 12:32

import datetime
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Activation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(db_column='user_id', null=True)),
                ('key', models.CharField(blank=True, max_length=100, null=True)),
                ('otp', models.PositiveIntegerField()),
                ('agent', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 9, 14, 18, 2, 15, 747087))),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(2023, 9, 16, 18, 2, 15, 747087))),
                ('email', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
            options={
                'db_table': 'account_activation',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('role_desc', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField(db_column='role_id')),
                ('user_id', models.IntegerField(db_column='user_id')),
            ],
            options={
                'db_table': 'user_role',
                'unique_together': {('role_id', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('id', models.AutoField(db_column='user_id', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('mobile_number', models.PositiveBigIntegerField(null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=40, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2023, 9, 14, 18, 2, 15, 745096))),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('alias', models.CharField(max_length=20, null=True, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_vendor_com_user', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user_profile',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
