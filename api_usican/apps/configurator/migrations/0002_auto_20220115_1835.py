# Generated by Django 3.1.13 on 2022-01-15 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customoptionitem',
            name='custom_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='configurator.customoption'),
        ),
    ]
