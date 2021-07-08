# Generated by Django 3.2.3 on 2021-07-03 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0065_auto_20210703_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Creative Designer', 'Creative Designer'), ('Job3', 'Job3'), ('Engineering', 'Engineering'), ('Finance', 'Finance'), ('Job2', 'Job2'), ('Job1', 'Job1')], max_length=225),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.coupon'),
        ),
    ]
