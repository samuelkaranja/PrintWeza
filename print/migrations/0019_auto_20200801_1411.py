# Generated by Django 3.0.7 on 2020-08-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0018_auto_20200801_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='extra',
            field=models.CharField(choices=[('10', '10'), ('50', '50'), ('30', '30')], max_length=100),
        ),
    ]