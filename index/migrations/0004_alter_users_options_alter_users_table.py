# Generated by Django 4.1.7 on 2023-03-04 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_users_time_start'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'managed': True, 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AlterModelTable(
            name='users',
            table='Users',
        ),
    ]
