# Generated by Django 4.1.2 on 2022-10-13 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20221013_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]