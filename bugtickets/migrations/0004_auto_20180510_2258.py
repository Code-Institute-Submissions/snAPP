# Generated by Django 2.0.5 on 2018-05-10 22:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugtickets', '0003_auto_20180510_1959'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bugupvote',
            unique_together={('bug_ticket', 'user', 'vote_type')},
        ),
    ]
