# Generated by Django 5.0 on 2024-05-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_players_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]