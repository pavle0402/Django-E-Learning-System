# Generated by Django 4.1.4 on 2023-06-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
