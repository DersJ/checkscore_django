# Generated by Django 2.1.5 on 2019-02-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0011_auto_20190208_0428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poolpageteaminfo',
            name='matched',
        ),
        migrations.AddField(
            model_name='poolpageteaminfo',
            name='match_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]