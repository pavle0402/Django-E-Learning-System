# Generated by Django 4.1.4 on 2023-06-23 11:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0015_feedback_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='ratings',
            field=models.PositiveIntegerField(default=None, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]