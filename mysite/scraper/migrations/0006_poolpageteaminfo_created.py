# Generated by Django 2.1.5 on 2019-02-05 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_scraperquery_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='poolpageteaminfo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]