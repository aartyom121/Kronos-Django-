# Generated by Django 5.0 on 2024-02-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_alter_players_amplua'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='amplua',
            field=models.CharField(choices=[('', 'Выберите амплуа'), ('Доигровщик', 'Доигровщик'), ('Центральный блокирующий', 'Центральный блокирующий'), ('Связующий', 'Связующий'), ('Диагональный', 'Диагональный'), ('Либеро', 'Либеро')], max_length=40, verbose_name='Амплуа'),
        ),
    ]
