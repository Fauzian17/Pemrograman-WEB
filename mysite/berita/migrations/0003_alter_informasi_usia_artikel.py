# Generated by Django 5.0.3 on 2024-05-13 06:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0002_alter_informasi_options_alter_katagori_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='informasi',
            name='usia',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('isi', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='berita.katagori')),
            ],
        ),
    ]
