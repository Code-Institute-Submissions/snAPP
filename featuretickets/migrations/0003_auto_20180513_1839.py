# Generated by Django 2.0.5 on 2018-05-13 18:39

from django.db import migrations, models
import featuretickets.models


class Migration(migrations.Migration):

    dependencies = [
        ('featuretickets', '0002_auto_20180513_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureticket',
            name='status',
            field=models.CharField(choices=[('todo', 'Pending'), ('doing', 'In Progress'), ('done', 'Complete')], default=featuretickets.models.default_status, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='featureticket',
            name='total_contributions',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]