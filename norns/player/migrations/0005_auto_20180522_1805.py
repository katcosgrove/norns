# Generated by Django 2.0.5 on 2018-05-22 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0004_inventory'),
        ('player', '0004_auto_20180522_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='health',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='player',
            name='inventory',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gear.Inventory'),
        ),
    ]
