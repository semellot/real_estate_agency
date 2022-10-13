# Generated by Django 4.1.2 on 2022-10-13 16:51

from django.db import migrations


def copy_owner_info(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            owner_name=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            defaults={
                'owner_pure_phone': flat.owner_pure_phone,
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(copy_owner_info),
    ]