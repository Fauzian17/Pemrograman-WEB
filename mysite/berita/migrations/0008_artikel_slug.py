# Generated by Django 5.0.3 on 2024-05-18 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0007_artikel_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]