# Generated by Django 4.2.2 on 2023-06-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_clients_diploma_alter_clients_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
