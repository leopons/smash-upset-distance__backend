# Generated by Django 3.1.2 on 2020-12-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upsets', '0005_auto_20201202_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='id',
        ),
        migrations.AlterField(
            model_name='set',
            name='original_id',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
