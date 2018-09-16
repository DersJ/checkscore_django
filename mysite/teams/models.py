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
	truck = Team(name="Truck Stop", city="Washington, D.C.", division=Team.OPEN, twitterHandle="truckstopulti", twitterLink="http://www.twitter.com/truckstopulti/")
	bravo = Team(name="Jonny Bravo", city="Denver, CO", division=Team.OPEN, twitterHandle="bravoultimate", twitterLink="http://www.twitter.com/bravoultimate/")
	ring = Team(name="Ring of Fire", city="Raleigh, N.C.", division=Team.OPEN, twitterHandle="ringultimate", twitterLink="http://www.twitter.com/ringultimate/")
	scandal = Team(name="Scandal", city="Washington, D.C.", division=Team.WOMENS, twitterHandle="scandalultimate", twitterLink="http://www.twitter.com/scandalultimate/")

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
	DIVISION_CHOICES = (
    ('O', 'Open'),
    ('X', 'Mixed'),
    ('W', 'Womens'),
    ('CO', 'College Open'),
    ('CW', 'College Open'),
    ('YO', 'Youth Open'),
    ('YX', 'Youth Mixed'),
    ('YW', 'Youth Womens'),)

	name = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	division = models.CharField(max_length=20, choices=DIVISION_CHOICES)
	#logo = models.FileField(null=True, blank=True)
	rosters = models.ManyToManyField('Roster', blank=True)
	twitterHandle = models.CharField(max_length=50, null=True)
	twitterLink = models.URLField(max_length=200, default='http://www.twitter.com')
	updated = models.DateTimeField(auto_now=True)
	


	def __str__(self):
		return self.name

	#def printStats(self):
	#	print(self.name+ " is from " + self.city + " and plays in the " + self.division.value.lower() + " division.")

#Players relate to teams and games through Rosters in a many to many relationship


class Person(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.first_name+" "+self.last_name

class Player(Person):
	career_goals=models.IntegerField(default=0)
	career_assists=models.IntegerField(default=0)
	career_blocks=models.IntegerField(default=0)
	#current_team = models.ForeignKey(Team, on_delete=models.CASCADE) to implement later
	

class Roster(models.Model):
	year = models.IntegerField(default=2018)
	associated_team = models.ForeignKey(Team, on_delete=models.CASCADE)
	#games = models.ManyToManyField(Game, blank = True, related_name='games')
	players = models.ManyToManyField(Player, through='RosterMembership', related_name='playsOn')
	updated = models.DateTimeField(auto_now=True)
	coaches = models.ManyToManyField(Person, through='RosterCoachMembership', related_name='coaches')

	def __str__(self):
		return self.associated_team.name + " " + str(self.year)


class Game(models.Model):
	date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	rosters = models.ManyToManyField(Roster, through='GameMembership')

#using extra fields in the many-to-many relationship between roster and player. Roster has members through RosterMembership
#https://docs.djangoproject.com/en/dev/topics/db/models/#extra-fields-on-many-to-many-relationships
class RosterMembership(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
	number = models.IntegerField(default=0)

	def __str__(self):
		return str(self.player)+" plays on "+str(self.roster)

class RosterCoachMembership(models.Model):
	ROLE_CHOICES = (
    ('H', 'Head'),
    ('A', 'Assistant'),)

	coach = models.ForeignKey(Person, on_delete=models.CASCADE)
	roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
	role = models.CharField(max_length=20, choices=ROLE_CHOICES)
	

	def __str__(self):
		return str(self.coach)+" coaches "+str(self.roster)

class GameMembership(models.Model):
	roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Tournament(models.Model):
	games = models.ManyToManyField(Game)
	teams = models.ManyToManyField(Team)