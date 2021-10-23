# Generated by Django 3.2.7 on 2021-10-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authetifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Patient'), (2, 'Doctor')], null=True),
        ),
    ]