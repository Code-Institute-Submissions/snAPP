# Generated by Django 2.0.5 on 2018-05-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('featuretickets', '0002_auto_20180512_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureticket',
            name='total_contributions',
            field=models.DecimalField(decimal_places=2, default=9.99, max_digits=8),
        ),
    ]