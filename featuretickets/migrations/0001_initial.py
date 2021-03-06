# Generated by Django 2.0.5 on 2018-06-09 02:57

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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateField(default=datetime.date.today)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(default=datetime.date.today, null=True)),
                ('date_started', models.DateField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('feature_type', models.CharField(choices=[('Convenience', 'Convenience'), ('Activity', 'Activity'), ('Security', 'Security'), ('Design', 'Design'), ('Other', 'Other')], max_length=30)),
                ('votes', models.IntegerField(default=0)),
                ('links', models.URLField(blank=True)),
                ('contribution', models.DecimalField(decimal_places=2, default=10.0, editable=False, max_digits=8)),
                ('target', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('report', models.TextField(null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_features', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='feature_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_comments', to='featuretickets.FeatureTicket'),
        ),
    ]
