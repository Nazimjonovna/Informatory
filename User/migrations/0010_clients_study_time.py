# Generated by Django 4.2.2 on 2023-06-25 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='study_time',
            field=models.CharField(blank=True, max_length=2500),
        ),
    ]