from django.db import models
from mysite import settings

# Create your models here.
class ScraperQuery(models.Model):
	class Meta:
		ordering = ['-created']
	TYPE_CHOICES = (
		('PP', "Pools Page"),
		('TP', "Team Page"),
		('ET', "Event Team Page"))

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scraper_queries')

	pageType = models.CharField(max_length=2, choices=TYPE_CHOICES, verbose_name="Page Type", help_text="Select your page type")
	url=models.URLField(verbose_name="URL", help_text="Link to a USA Ultimate page")
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		formatedDate = self.created.strftime("%m/%d/%Y, %I:%M:%S %p")
		return '%s query at %s' % (self.get_pageType_display(), formatedDate)

class PoolPageTeamInfo(models.Model):
	name = models.CharField(max_length=200)
	seed = models.IntegerField()
	poolSeed = models.IntegerField(default=0)
	eventTeamURL = models.URLField()
	created = models.DateTimeField(auto_now_add=True)
	query = models.ForeignKey(ScraperQuery, on_delete=models.CASCADE, related_name='teams')

	def __str__(self):
		return '%s seeded %s' % (self.name, self.seed)



