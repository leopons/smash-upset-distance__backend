# Generated by Django 3.1.2 on 2020-12-10 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upsets', '0006_auto_20201210_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='set',
            old_name='original_id',
            new_name='id',
        ),
    ]
