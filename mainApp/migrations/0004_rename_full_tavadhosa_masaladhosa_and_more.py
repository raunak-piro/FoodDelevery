# Generated by Django 4.1.2 on 2022-12-07 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_tavadhosa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tavadhosa',
            old_name='full',
            new_name='masaladhosa',
        ),
        migrations.RenameField(
            model_name='tavadhosa',
            old_name='half',
            new_name='paneerdhosa',
        ),
    ]