# Generated by Django 3.0.8 on 2020-11-27 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201127_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredients',
            new_name='ingridients',
        ),
    ]
