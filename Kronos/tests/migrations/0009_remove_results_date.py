# Generated by Django 5.0 on 2024-05-27 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_results_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='date',
        ),
    ]