# Generated by Django 3.2.3 on 2021-07-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_auto_20210703_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='color',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Creative Designer', 'Creative Designer'), ('Finance', 'Finance'), ('Job2', 'Job2'), ('Engineering', 'Engineering'), ('Job1', 'Job1'), ('Job3', 'Job3')], max_length=225),
        ),
    ]
