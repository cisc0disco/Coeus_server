# Generated by Django 3.1.7 on 2021-02-24 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homedata_voice_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homedata',
            old_name='voice_gender',
            new_name='voice',
        ),
    ]
