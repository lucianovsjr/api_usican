# Generated by Django 3.1.13 on 2022-01-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20220122_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetrequest',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
