# Generated by Django 5.0 on 2024-03-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_rename_result_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='ans',
            new_name='ans1',
        ),
    ]