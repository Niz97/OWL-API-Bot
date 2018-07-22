import requests
import json
import sys


# Get the response from the API endpoint.
URL = requests.get("https://api.overwatchleague.com/stats/players?stage_id=regular_season")
STATS = URL.json()['data']

# read in player from command line argument
player_name = sys.argv[1]

class Setup():

	def __init__(self, ply):
		player = ply
		self.name = player["name"]
		self.role = player["role"]
		self.team = player["team"]
		self.elim_avg_10 = player["eliminations_avg_per_10m"]
		self.death_avg_10 = player["deaths_avg_per_10m"]
		self.hero_dmg_avg_10 = player["hero_damage_avg_per_10m"]
		self.heal_avg_10 = player["healing_avg_per_10m"]
		self.ult_earned_avg_10 = player["ultimates_earned_avg_per_10m"]
		self.final_blows_avg_10 = player["final_blows_avg_per_10m"]
		self.total_time_played = player["time_played_total"]

	def elim_and_death_avg_per_10(self):
		print("Player: {}".format(self.name))
		print("Average eliminnations per 10 minutes: {:.2f}".format(self.elim_avg_10))
		print("Average deaths per 10 minutes: {:.2f}".format(self.death_avg_10))

	def all_stats(self):
		reply = None
		reply = RESPONSE.format(
			self.name,
			self.team,
			self.role,
			self.elim_avg_10,
			self.death_avg_10,
			self.hero_dmg_avg_10,
			self.heal_avg_10,
			self.ult_earned_avg_10,
			self.final_blows_avg_10,
			self.total_time_played / 60 / 60
			)
		return reply


# format all stats for player
RESPONSE = (
	"Statistics for {}\n"
	"Team:{:>41}\n"
	"Role:{:>45}\n"
	"Average eliminations per 10 min: {:>14.2f}\n"
	"Average deaths per 10 min:{:>21.2f}\n"
	"Average hero damage per 10 min:{:>18.2f}\n"
	"Average healing per 10 min:{:>21.2f}\n"
	"Average ultimates earned per 10 min:{:>11.2f}\n"
	"Average final blows per 10 min:{:>16.2f}\n"
	"Total time played:{:>30.2f}\n"
	)

# loop through STATS to find profile that corresponds to user given name
def load_player():
	for player_profile in STATS:
		# print(player_profile)
		if player_profile["name"].lower() == player_name.lower():
			#print(player_profile)
			return player_profile
		else:
			print("This player does not exist")
			exit()

# Class to setup and object to access all stats



# pull stats for player and save to variable
player_stats = load_player()

# setup object and pass stats to the instance
player = Setup(player_stats)


print(player.all_stats())

# TODO
