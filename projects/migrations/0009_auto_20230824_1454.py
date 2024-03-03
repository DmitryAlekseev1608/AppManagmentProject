# Generated by Django 3.2.20 on 2023-08-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20230824_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financialproject2023',
            old_name='fact_stage',
            new_name='fact_stage_consider',
        ),
        migrations.RenameField(
            model_name='financialproject2023',
            old_name='plan_stage',
            new_name='fact_stage_work',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='reason',
        ),
        migrations.AddField(
            model_name='financialproject2023',
            name='plan_stage_consider',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='financialproject2023',
            name='plan_stage_work',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='financialproject2023',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]