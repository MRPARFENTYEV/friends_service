# Generated by Django 5.0.6 on 2024-05-23 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_friends_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_id', models.CharField(max_length=50)),
                ('is_hidden', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweet_friends_app.user')),
            ],
            options={
                'verbose_name': 'Друг',
                'verbose_name_plural': 'Друзья',
            },
        ),
    ]
