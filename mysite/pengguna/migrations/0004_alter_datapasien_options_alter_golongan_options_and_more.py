# Generated by Django 5.0.3 on 2024-03-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0003_alter_datapasien_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datapasien',
            options={'verbose_name_plural': '2. Biodata'},
        ),
        migrations.AlterModelOptions(
            name='golongan',
            options={'verbose_name_plural': '3. Golongan'},
        ),
        migrations.AlterModelOptions(
            name='rumahsakit',
            options={'verbose_name_plural': '1. Rumah Sakit'},
        ),
    ]