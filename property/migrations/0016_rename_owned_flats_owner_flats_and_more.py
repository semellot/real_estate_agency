# Generated by Django 4.1.2 on 2022-10-18 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_alter_complaint_complainant_alter_complaint_flat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owned_flats',
            new_name='flats',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]