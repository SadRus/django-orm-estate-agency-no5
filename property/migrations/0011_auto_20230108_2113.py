# Generated by Django 3.2 on 2023-01-08 18:13

from django.db import migrations


def migrate_owners_data(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phonenumber=flat.owner_pure_phone,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20230108_0206'),
    ]

    operations = [
        migrations.RunPython(migrate_owners_data),
    ]
