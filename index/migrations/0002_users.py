# Generated by Django 4.1.7 on 2023-03-04 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=120, verbose_name='用户名')),
                ('password', models.CharField(max_length=120, verbose_name='用户名')),
                ('photo', models.ImageField(upload_to='media/users/photo', verbose_name='头像')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('is_active', models.IntegerField(default=1, verbose_name='状态')),
            ],
        ),
    ]
