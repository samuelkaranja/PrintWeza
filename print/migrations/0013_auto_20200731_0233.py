# Generated by Django 3.0.7 on 2020-07-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0012_auto_20200731_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='color',
            field=models.CharField(choices=[('5', 'Black (Kshs 5)'), ('10', 'Colored (Kshs 10)')], max_length=100),
        ),
    ]
