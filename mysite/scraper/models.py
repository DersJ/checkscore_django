from django.db import models

# Create your models here.
class ScraperQuery(models.Model):
	TYPE_CHOICES = (
		('PP', "Pools Page"),
		('TP', "Team Page"),
		('ET', "Event Team Page"))

	pageType = models.CharField(max_length=2, choices=TYPE_CHOICES, verbose_name="Page Type", help_text="Select your page type")
	url=models.URLField(verbose_name="URL", help_text="Link to a USA Ultimate page")

class PoolPageTeamInfo(models.Model):
	name = models.CharField(max_length=200)
	seed = models.IntegerField()
	poolSeed = models.IntegerField(default=0)
	eventTeamURL = models.URLField()



