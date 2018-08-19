# Generated by Django 2.0.5 on 2018-08-19 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('featuretickets', '0003_auto_20180819_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='feature_ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feature_comments', to='featuretickets.FeatureTicket'),
        ),
        migrations.AlterField(
            model_name='featureticket',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_features', to=settings.AUTH_USER_MODEL),
        ),
    ]
