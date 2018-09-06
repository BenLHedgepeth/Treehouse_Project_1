import csv

def players_registeration(file):
	'''Create a file that collects all information about soccer participants'''

	with open(file) as signup_data:
		registeration_info = csv.DictReader(signup_data)
		players_data = list(registeration_info)

	return players_data


def player_organizer(players):
	'''Distinguish between players that have experience/no experience playing soccer'''
	
	player_experience = {}

	for player in players:
		experience_type = player.get("Soccer Experience")

		if experience_type == "YES":
			player_experience.setdefault("Experienced", [])
			player_experience["Experienced"].append(player)
		else:
			player_experience.setdefault("Not Experienced", [])
			player_experience["Not Experienced"].append(player)

	return player_experience	


def team_lineups(soccer_teams):
	'''Create a file that organizes 'all' soccer players into their teams'''
	
	with open('teams.txt', 'w') as rosters:
		player_roster = ''
		for team in soccer_teams.keys():
			player_roster += '{team}\n'.format(team=team)

			teammates = soccer_teams[team]	
			for teammate in teammates:
				player_roster += "{name}, {experience}, {guardians}\n".format(name=teammate['Name'], experience=teammate['Soccer Experience'], guardians=teammate['Guardian Name(s)'])
			player_roster += '\n'	
		rosters.write(player_roster)


def team_greeting(soccer_groups):
	for group, players in soccer_groups.items():
		for _ in range(len(players)):
			filename = "_".join(players[_]['Name'].split(" ")).lower()
			
			with open(f'{filename}.txt', 'w') as soccer_newsletter:
				letter = """\tDear {guardians},\n
				The beginning of our new soccer season is soon approaching. We're excited for {person}
				to be a part of the {team_name}'s! Just as a reminder the team will practice 2 times a week;
				Tuesdays and Thursdays.	Our first practice is scheduled for Tuesday, September, 4.
				""".format(guardians=players[_]['Guardian Name(s)'], person=players[_]['Name'], team_name=group)

				letter += '\n\n\t - Soccer League Coordinator'

				soccer_newsletter.write(letter)
			
if __name__ == '__main__':

	teams = {
		"Sharks" : [],
		"Dragons" : [],
		"Raptors" : []
	}

	players_signed_up = players_registeration("soccer_players.csv")

	experience_levels = player_organizer(players_signed_up)
	players_left = experience_levels.copy()
	
	for team in teams.keys():
		for level, team_players in players_left.items():
			i = 0
			while i < 3:
				player_pick = team_players.pop(0)
				teams[team].append(player_pick)
				i += 1
			
			players_left[level] = team_players
			
	soccer_team_rivals = team_lineups(teams)

	practice_notice = team_greeting(teams)
		
	
