# Generated by Django 4.1.5 on 2023-02-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quoting", "0007_remove_line_quote_quote_lines"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quote",
            name="lines",
        ),
        migrations.AddField(
            model_name="line",
            name="quote",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="quoting.quote",
            ),
            preserve_default=False,
        ),
    ]
