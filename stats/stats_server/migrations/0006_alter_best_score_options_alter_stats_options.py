# Generated by Django 4.2.1 on 2023-05-23 12:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("stats_server", "0005_best_score_rename_best_score_stats_all_gold_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="best_score",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="stats",
            options={"ordering": ["id"]},
        ),
    ]
