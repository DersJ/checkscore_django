# Generated by Django 2.1.5 on 2019-02-07 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0009_auto_20190207_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poolpageteaminfo',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='scraper.ScraperQuery'),
        ),
    ]
