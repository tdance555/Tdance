# Generated by Django 5.0.7 on 2024-08-01 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_trip_delete_post1_delete_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='vendor_icon',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='vendor_id',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='vendor_name',
            new_name='title',
        ),
    ]
