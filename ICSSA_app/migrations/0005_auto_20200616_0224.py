# Generated by Django 3.0.7 on 2020-06-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ICSSA_app', '0004_auto_20200615_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='executivetenure',
            name='members',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pollquestion',
            name='choices',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
