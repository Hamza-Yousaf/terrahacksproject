# Generated by Django 5.0.7 on 2024-08-03 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environmentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='score_worth',
            field=models.IntegerField(default=0),
        ),
    ]
