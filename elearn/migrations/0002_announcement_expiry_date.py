# Generated by Django 4.1.4 on 2023-07-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='expiry_date',
            field=models.DateTimeField(null=True),
        ),
    ]
