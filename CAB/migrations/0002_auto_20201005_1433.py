# Generated by Django 3.1.2 on 2020-10-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab',
            name='convenio',
            field=models.BigIntegerField(),
        ),
    ]
