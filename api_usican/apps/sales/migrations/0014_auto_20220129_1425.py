# Generated by Django 3.1.13 on 2022-01-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0013_auto_20220129_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetrequest',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
