# Generated by Django 4.2.9 on 2024-11-12 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Фото локации'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Локация'),
        ),
        migrations.AddIndex(
            model_name='placeimage',
            index=models.Index(fields=['ordinal_number'], name='places_plac_ordinal_e1bcc4_idx'),
        ),
    ]