# Generated by Django 2.2 on 2019-04-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_ticket_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]