# Generated by Django 3.1.13 on 2021-10-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20210918_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
    ]