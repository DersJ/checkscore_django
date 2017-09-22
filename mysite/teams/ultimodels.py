import tweepy
import re
from enum import Enum

class GameState(Enum):
	FUTURE = "hasn't started"
	INPROGRESS = "is in Progress"
	FINISHED = "has finished"

class Division(Enum):
	OPEN = "Open"
	MIXED = "Mixed"
	WOMENS = "Womens"
	COLLEGEOPEN = "College Open"
	COLLEGEWOMENS = "College Womens"
	YOUTHOPEN = "Youth Open"
	YOUTHMIXED = "Youth Mixed"
	YOUTHWOMENS = "Youth Womens"

class Team:
	def __init__(self, name, city, division, twitterHandle, nicknames=[]):
		self.name = name
		self.city = city
		self.division = division
		self.twitterHandle = twitterHandle
		self.nicknames = nicknames

	def printStats(self):
		print(self.name+ " is from " + self.city + " and plays in the " + self.division.value.lower() + " division.")




class Game:
	def __init__(self, team0, team1, start_time, winning_score=15, point_cap=17, soft_cap=80, hard_cap=90): #teams are Team objects, start_time is datetime obj, scores and caps are ints

		self.scores = {team0 : 0, team1 : 0}

		self.team0 = team0
		self.team1 = team1
		self.start_time = start_time

		self.winning_score = winning_score
		self.point_cap = point_cap

		self.soft_cap = 80
		self.hard_cap = 90

		#TODO: Implement date/time verification
	def printInfo(self):
		print(self.team0.name + " plays " + self.team1.name + " at " + self.start_time.ctime + " in a game to " + str(self.winning_score))

	def increment_score(self, team):
		self.scores[team] = self.scores[team] + 1

	def setScore(self, team, score):
		self.scores[team] = score

	def getTeams(self):
		return([team0, team1])


	def validateScores():
		team0_score = self.scores[team0]
		team1_score = self.scores[team1]
		if((team0_score  > self.winning_score or team1_score > self.winning_score) and (abs(team0_score-team1_score) > 1)):
			pass


class Tournament:
	def __init__(self):
		self.divisons = {}

	def addDivision(self, division,):
		if(self.divisions.get(division.divisionType)):
			#throw exception
			pass
		self.divions[division.divisionType] = division


class TournamentDivision:
	def __init__(self, divisionType, numTeams, teams=[]):
		self.divsionType = divsionType
		self.numTeams = numTeams
		self.teams = teams

	def addUsauPage(self, link):
		self.usauLink = link
	def addTeam(self, team):
		self.teams.append(team)

	def createPooledTeams(self, numPools): #This functino assumes self.teams contains seeded teams
		pooledTeams = []
		for i in range(numPools):
			pooledTeams.append([])
		for i in range(len(teams)):
			if((i//8) %2 == 0):
				if((i//4) % 2 == 0) :
					pooledTeams[i%4].append(self.teams[i])
				else:
					pooledTeams[3-(i%4)].append(self.teams[i])
			else:
				if((i//4) % 2 == 1) :
					pooledTeams[i%4].append(self.teams[i])
				else:
					pooledTeams[3-(i%4)].append(self.teams[i])
		return pooledTeams


	def createPools(self, numPools, pooledTeams=[]):
		if not pooledTeams:
			pooledTeams = self.createPooledTeams(numPools)
		self.pools = []
		for i in range(numPools):
			pools.append(Pool(pooledTeams[i]))



class Pool:
	def __init__(self, teams):
		self.teams = teams

class Round:
	def __init__(self, times):
		pass




class TweepyScraper:
	def __init__(self):
		consumer_key = "W0WLx3Fo6N7A8ODfl9r0YhTGF"
		access_token = 	"890385029964201984-ynQaG4cRTa5JMJeApX8Ae9ue3uFuiE2"

		file = open("keys.txt", 'r')
		consumer_secret = file.readline()[:-1]
		access_token_secret = file.readline()[:-1]
		file.close()


		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		self.api = tweepy.API(auth)

	def pull_recent_tweets(self, team, num=20):
		tweets = self.api.user_timeline(team.twitterHandle, count=num)

		final = []

		for tweet in tweets:
			final.append(tweet.text)

		return final

class Scraper:
	def __init__(self):
		self.tweepy_scraper = TweepyScraper()
		self.beatiful_soup = None #TODO: IMPLEMENT BS

		#impl everything

	def parseTweet(tweet):
		query = tweet.replace(" ", "")

		regex = r'[0-9]+-+[0-9]+'
		match = re.search(regex, query)
		if(match):
			return match.group(0)
		else:
			return None

	def check_for_score_update(self, game):
		teams = game.getTeams()

		team0_tweets = ts.pull_recent_tweets(teams[0])
		team0_most_recent_score = None

		team0score = None
		team1score = None

		for tweet in team0_tweets:
			parsed = parseTweet(tweet)
			if(parsed):
				team0_most_recent_score = parsed
				break

		team1_tweets = ts.pull_recent_tweets(teams[1])
		team1_most_recent_score = None

		for tweet in team1_tweets:
			parsed = parseTweet(tweet)
			if(parsed):
				team1_most_recent_score = parsed
				break

		if(team0_most_recent_score):
			team0score = team0_most_recent_score.split('-')[0]
			team1score = team0_most_recent_score.split('-')[1]

		if(team1_most_recent_score):
			team0score = team1_most_recent_score.split('-')[0]
			team1score = team1_most_recent_score.split('-')[1]

		if(team0score or team1score):
			game.setScore(teams[0], team0score)
			game.setScore(teams[1], team1score)