# Generated by Django 3.1.2 on 2020-10-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PAF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportarPAF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='excel')),
                ('timestamp', models.DateField(auto_now=True)),
                ('subido', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='paf',
            name='timestamps',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
