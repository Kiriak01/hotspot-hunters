# Generated by Django 4.2.1 on 2023-06-26 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]
