# Generated by Django 3.2.3 on 2021-07-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0066_auto_20210703_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Job3', 'Job3'), ('Job2', 'Job2'), ('Finance', 'Finance'), ('Creative Designer', 'Creative Designer'), ('Engineering', 'Engineering'), ('Job1', 'Job1')], max_length=225),
        ),
    ]
