# Generated by Django 2.2 on 2019-04-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190405_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='description',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
