# Generated by Django 4.2.6 on 2023-10-20 17:20

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("fe_cr", "0003_strategy"),
    ]

    operations = [
        migrations.CreateModel(
            name="StrategyExecution",
            fields=[
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("initial_cash", models.DecimalField(decimal_places=2, max_digits=10)),
                ("final_cash", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total_return", models.DecimalField(decimal_places=2, max_digits=10)),
                ("num_trades", models.IntegerField()),
                ("num_win", models.IntegerField()),
                ("strategy", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="fe_cr.strategy")),
                ("ticker", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="fe_cr.ticker")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
