# Generated by Django 5.0.7 on 2024-08-24 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0003_donors_email_donors_mobile_donors_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donors',
            old_name='distrcitId',
            new_name='districtId',
        ),
    ]
