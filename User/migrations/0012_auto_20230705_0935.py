# Generated by Django 3.2.19 on 2023-07-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_consulting_clients_consulting_university_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='ID_raqam',
        ),
        migrations.AddField(
            model_name='consulting',
            name='ID_raqam',
            field=models.CharField(default=1, max_length=2500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consulting',
            name='director',
            field=models.CharField(default=1, max_length=2500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consulting',
            name='place_office',
            field=models.CharField(default=1, max_length=25000000),
            preserve_default=False,
        ),
    ]