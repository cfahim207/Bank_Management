# Generated by Django 5.0.6 on 2024-07-11 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='birthday',
            new_name='birth_date',
        ),
    ]
