# Generated by Django 4.2.6 on 2024-01-01 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_cartdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdb',
            old_name='Username',
            new_name='name',
        ),
    ]
