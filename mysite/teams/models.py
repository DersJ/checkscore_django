from django.db import models
from enum import Enum
#from ultimodels import *
# Create your models here.
import pickle

""" DEFAULTS:
	truck = Team("Truck Stop", "Washington, D.C.", Division.OPEN, "truckstopulti")
    bravo = Team("Jonny Bravo", "Denver, CO", Division.OPEN, "bravoultimate")
    ring = Team("Ring of Fire", "Raleigh, N.C.", Division.OPEN, "ringultimate")
    scandal = Team("Scandal", "Washington, D.C.", Division.WOMENS, "scandalultimate")"""

def addTeams(teams):
	old_teams = pickle.load(open('teams.p', 'rb'))

	for i in teams:
		old_teams.append(i)

	pickle.dump(old_teams, open('teams.p', 'wb'))


def teamslist():
	#return pickle.load(open('./teams/teams.p', 'rb'))
	truck = Team(name="Truck Stop", city="Washington, D.C.", division='Division.OPEN', twitterHandle="truckstopulti", twitterLink="http://www.twitter.com/truckstopulti/")
	bravo = Team(name="Jonny Bravo", city="Denver, CO", division='Division.OPEN', twitterHandle="bravoultimate", twitterLink="http://www.twitter.com/bravoultimate/")
	ring = Team(name="Ring of Fire", city="Raleigh, N.C.", division='Division.OPEN', twitterHandle="ringultimate", twitterLink="http://www.twitter.com/ringultimate/")
	scandal = Team(name="Scandal", city="Washington, D.C.", division='Division.WOMENS', twitterHandle="scandalultimate", twitterLink="http://www.twitter.com/scandalultimate/")

	truck.save()
	bravo.save()
	ring.save()
	scandal.save()


class Division(Enum):
	OPEN = "Open"
	MIXED = "Mixed"
	WOMENS = "Womens"
	COLLEGEOPEN = "College Open"
	COLLEGEWOMENS = "College Womens"
	YOUTHOPEN = "Youth Open"
	YOUTHMIXED = "Youth Mixed"
	YOUTHWOMENS = "Youth Womens"

class Team(models.Model):
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	division = models.CharField(max_length=50)
	twitterHandle = models.CharField(max_length=50)
	twitterLink = models.URLField(max_length=200, default='http://www.twitter.com')


	def __unicode__(self):
		return self.name

	def printStats(self):
		print(self.name+ " is from " + self.city + " and plays in the " + self.division.value.lower() + " division.")