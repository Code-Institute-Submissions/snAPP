# Generated by Django 2.0.5 on 2018-06-07 13:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', null=True, upload_to='images')),
                ('trade_union', models.CharField(default='', max_length=100, null=True)),
                ('description', models.TextField(default='', null=True)),
                ('alert', models.TextField(default='No active alerts.', null=True)),
                ('alert_date', models.DateField(default=datetime.date.today, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
