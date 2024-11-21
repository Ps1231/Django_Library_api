# Generated by Django 5.1.3 on 2024-11-21 17:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_loan_borrowed_at_remove_loan_returned_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='is_returned',
        ),
        migrations.AddField(
            model_name='loan',
            name='borrowed_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='returned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]