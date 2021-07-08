# Generated by Django 3.2.3 on 2021-06-18 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.coupon'),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Finance', 'Finance'), ('Engineering', 'Engineering'), ('Creative Designer', 'Creative Designer')], max_length=225),
        ),
    ]
