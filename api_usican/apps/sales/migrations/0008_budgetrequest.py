# Generated by Django 3.1.13 on 2022-01-22 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("configurator", "0002_auto_20220115_1835"),
        ("sales", "0007_auto_20211120_2133"),
    ]

    operations = [
        migrations.CreateModel(
            name="BudgetRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deadline", models.DateField(blank=True, null=True)),
                ("observation", models.TextField(blank=True)),
                ("observation_reason", models.TextField(blank=True)),
                ("informed_customer_decline", models.BooleanField(default=False)),
                (
                    "contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="sales.contact",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="sales.customer"
                    ),
                ),
                (
                    "means_receipt",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="budget_request_means_receipt_set",
                        to="configurator.customoptionitem",
                    ),
                ),
                (
                    "reason_decline",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="budget_request_reason_decline_set",
                        to="configurator.customoptionitem",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="budget_request_status_set",
                        to="configurator.customoptionitem",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
