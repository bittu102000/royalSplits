# Generated by Django 3.2.3 on 2021-06-06 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210606_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail_1', models.ImageField(upload_to='images/')),
                ('thumbnail_2', models.ImageField(upload_to='images/')),
                ('thumbnail_3', models.ImageField(upload_to='images/')),
                ('thumbnail_4', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
