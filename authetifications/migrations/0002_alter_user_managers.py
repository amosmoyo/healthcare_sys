# Generated by Django 3.2.7 on 2021-10-04 12:47

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('authetifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('oobjects', django.db.models.manager.Manager()),
            ],
        ),
    ]
