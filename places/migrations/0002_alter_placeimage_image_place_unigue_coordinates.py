# Generated by Django 4.2.9 on 2024-11-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фото локации'),
        ),
        migrations.AddConstraint(
            model_name='place',
            constraint=models.UniqueConstraint(fields=('longitude', 'latitude'), name='unigue_coordinates'),
        ),
    ]