# Generated by Django 4.1.7 on 2023-03-04 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='时间'),
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('time', models.TimeField(auto_now=True, verbose_name='创建时间')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.films', verbose_name='用户名')),
            ],
        ),
    ]