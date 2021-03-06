# Generated by Django 3.1 on 2020-08-28 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200828_0532'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarangayBuoy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=220)),
                ('municipality', models.CharField(max_length=220)),
                ('barangay', models.CharField(max_length=220)),
                ('buoy_number', models.PositiveIntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Intruder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=220)),
                ('municipality', models.CharField(max_length=220)),
                ('barangay', models.CharField(max_length=220)),
                ('buoy_number', models.PositiveIntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='salesman',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
