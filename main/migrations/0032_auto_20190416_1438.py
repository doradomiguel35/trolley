# Generated by Django 2.2 on 2019-04-16 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_checklist_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='lists',
        ),
        migrations.DeleteModel(
            name='Checklist',
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
    ]
