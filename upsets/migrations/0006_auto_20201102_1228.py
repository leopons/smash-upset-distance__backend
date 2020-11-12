# Generated by Django 3.1.2 on 2020-11-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upsets', '0005_upsettreenode'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tournament',
            index=models.Index(fields=['-start_date'], name='upsets_tour_start_d_e6907b_idx'),
        ),
    ]