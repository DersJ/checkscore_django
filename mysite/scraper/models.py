from django.db import models

# Create your models here.
class ScraperQuery(models.Model):
	TYPE_CHOICES = (
		('PP', "Pools Page"),
		('TP', "Team Page"),
		('ET', "Event Team Page"))

	pageType = models.CharField(max_length=2, choices=TYPE_CHOICES)
	url=models.URLField()
