# Generated by Django 3.2.20 on 2023-08-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_projects_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialproject2023',
            name='number_row',
            field=models.TextField(blank=True, null=True),
        ),
    ]