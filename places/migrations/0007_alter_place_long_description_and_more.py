# Generated by Django 4.2.9 on 2024-11-14 07:08

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_title_alter_placeimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, default=' ', verbose_name='Полное описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, default='', verbose_name='Короткое описание'),
            preserve_default=False,
        ),
    ]