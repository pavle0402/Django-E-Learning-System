# Generated by Django 4.1.4 on 2023-06-20 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elearn.course'),
        ),
    ]