# Generated by Django 5.1.3 on 2024-11-21 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='borrowed_at',
        ),
        migrations.RemoveField(
            model_name='loan',
            name='returned_at',
        ),
    ]