# Generated by Django 2.0.5 on 2018-05-30 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('featuretickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('street_address1', models.CharField(max_length=40)),
                ('street_address2', models.CharField(max_length=40)),
                ('town_or_city', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features_vote', to='featuretickets.FeatureTicket')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
            ],
        ),
    ]
