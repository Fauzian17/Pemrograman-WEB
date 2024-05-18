# Generated by Django 5.0.3 on 2024-03-24 07:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapasien',
            name='ruangan',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='RumahSakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_RS', models.CharField(max_length=255)),
                ('alamat_RS', models.CharField(max_length=255)),
                ('data_pasien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pengguna.datapasien')),
            ],
        ),
        migrations.CreateModel(
            name='Golongan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_BPJS', models.CharField(max_length=255)),
                ('keterangan', models.CharField(max_length=255)),
                ('rumah_sakit', models.ManyToManyField(to='pengguna.rumahsakit')),
            ],
        ),
    ]
