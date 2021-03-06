# Generated by Django 2.1.5 on 2019-02-13 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0012_auto_20190208_0431'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('division', models.CharField(max_length=20)),
                ('twitterLink', models.URLField(default='http://www.twitter.com')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='scraper.ScraperQuery')),
            ],
        ),
    ]
