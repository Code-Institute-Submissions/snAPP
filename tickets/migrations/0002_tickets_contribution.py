# Generated by Django 2.0.5 on 2018-05-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='contribution',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=6),
        ),
    ]
