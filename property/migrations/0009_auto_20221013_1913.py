# Generated by Django 4.1.2 on 2022-10-13 16:13

from django.db import migrations
import phonenumbers

def fill_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number_for_region(parsed_number, 'RU'):
            flat.owner_pure_phone = phonenumbers.format_number(
                parsed_number,
                phonenumbers.PhoneNumberFormat.E164
            )
            flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone_alter_flat_liked_user'),
    ]

    operations = [
        migrations.RunPython(fill_pure_phone),
    ]
