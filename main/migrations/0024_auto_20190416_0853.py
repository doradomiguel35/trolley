# Generated by Django 2.2 on 2019-04-16 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_checklist_progress'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Checklist',
        ),
        migrations.DeleteModel(
            name='Progress',
        ),
    ]
