# Generated by Django 4.2.1 on 2023-07-09 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poi', '0006_pointofinterest_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('radius', models.IntegerField(blank=True, default=10000, null=True)),
                ('poi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poi.pointofinterest')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]