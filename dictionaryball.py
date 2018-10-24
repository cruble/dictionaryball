game_dictionary = {
    'away': {
        'colors': ['Turquoise', 'Purple'],
        'players': {
            'Ben Gordon': {
                'assists': 2,
                'blocks': 2,
                'number': 8,
                'points': 33,
                'rebounds': 3,
                'shoe': 15,
                'slam_dunks': 0,
                'steals': 2
            },
            'Bismak Byombo': {
                'assists': 7,
                'blocks': 15,
                'number': 0,
                'points': 12,
                'rebounds': 4,
                'shoe': 16,
                'slam_dunks': 10,
                'steals': 7
            },
            'Brendan Haywood': {
                'assists': 2,
                'blocks': 2,
                'number': 8,
                'points': 33,
                'rebounds': 3,
                'shoe': 15,
                'slam_dunks': 0,
                'steals': 2
            },
            'DeSagna Diop': {
                'assists': 12,
                'blocks': 5,
                'number': 2,
                'points': 24,
                'rebounds': 12,
                'shoe': 14,
                'slam_dunks': 5,
                'steals': 4
            },
            'Jeff Adrien': {
                'assists': 1,
                'blocks': 7,
                'number': 4,
                'points': 10,
                'rebounds': 1,
                'shoe': 18,
                'slam_dunks': 2,
                'steals': 2
            }
        },
        'team_name': 'Charlotte Hornets'
    },
    'home': {
        'colors': ['Black', 'White'],
        'players': {
            'Alan Anderson': {
                'assists': 12,
                'blocks': 1,
                'number': 0,
                'points': 22,
                'rebounds': 12,
                'shoe': 16,
                'slam_dunks': 1,
                'steals': 3
            },
            'Brook Lopez': {
                'assists': 10,
                'blocks': 1,
                'number': 11,
                'points': 17,
                'rebounds': 19,
                'shoe': 17,
                'slam_dunks': 15,
                'steals': 3
            },
            'Jason Terry': {
                'assists': 2,
                'blocks': 11,
                'number': 31,
                'points': 19,
                'rebounds': 2,
                'shoe': 15,
                'slam_dunks': 1,
                'steals': 4
            },
            'Mason Plumlee': {
                'assists': 6,
                'blocks': 8,
                'number': 1,
                'points': 26,
                'rebounds': 12,
                'shoe': 19,
                'slam_dunks': 5,
                'steals': 3
            },
            'Reggie Evans': {
                'assists': 12,
                'blocks': 12,
                'number': 30,
                'points': 12,
                'rebounds': 12,
                'shoe': 14,
                'slam_dunks': 7,
                'steals': 12
            }
        },
        'team_name': 'Brooklyn Nets'
    }
}


def game_dict():
	return game_dictionary

def all_players(): 
	pass 


def num_points_scored(player_name):
	points = 0 
	for location, team_stats in game_dict().items():
		for stats, data in team_stats.items():
			if stats == "players" and player_name in data:
				points = data[player_name]['points']
	return points 

def shoe_size(player_name):
	size = 0
	for location, team_stats in game_dict().items():
		for stats, data in team_stats.items():
			if stats == "players" and player_name in data:
				size = data[player_name]['shoe']
	return size
	#print("hello")

def team_colors(input_team_name):
	team_location = ''
	for location, team_stats in game_dict().items():
		for stats, data in team_stats.items():
			#import pdb; pdb.set_trace()
			if stats == "team_name" and input_team_name == game_dict()[location]['team_name']: 
				team_location = location
	return game_dict()[team_location]['colors']

def team_names():
	team_name_list = []
	for location, team_stats in game_dict().items():
		for stats, data in team_stats.items():
			#import pdb; pdb.set_trace()
			if stats == "team_name":
				team_name_list.append(data)
	return team_name_list

def player_numbers(input_team_name):
	team_jersey_numbers = []
	for location, team_stats in game_dict().items():
		for stats, data in team_stats.items():
		#import pdb; pdb.set_trace()()
			if stats == "players" and game_dict()[location]['team_name'] == input_team_name:
				#import pdb; pdb.set_trace()
				for p, s in data.items():
					team_jersey_numbers.append(s['number'])
					print(p, s['number'])
	print(team_jersey_numbers)
	return team_jersey_numbers

def player_stats(player_name):
	for location, team_stats in game_dict().items():
		for stats, data in team_stats.items():
			#import pdb; pdb.set_trace()
			if stats == "players" and player_name in data:
			 	for p, s in data.items(): 
			 		if p == player_name: 
			 			return s 

def all_players(): 
	players = []
	for location, team_stats in game_dict().items():
		for stats, data in team_stats.items():
			#import pdb; pdb.set_trace()
			if stats == "players":
			 	for p, s in data.items(): 
			 		players.append(p)
	return players 

def players_with_shoes(list_of_players):
	player_dict = {}
	for player in list_of_players:
		for location, team_stats in game_dict().items():
			for stats, data in team_stats.items():
				#import pdb; pdb.set_trace()
				if stats == "players":
				 	for p, s in data.items(): 
				 		player_dict[p] = s['shoe']
	return player_dict

def players_points(list_of_players):
	player_dict = {}
	for player in list_of_players:
		for location, team_stats in game_dict().items():
			for stats, data in team_stats.items():
				#import pdb; pdb.set_trace()
				if stats == "players":
				 	for p, s in data.items(): 
				 		player_dict[p] = s['points']
	return player_dict
				 		


def big_shoe_rebounds(): 
	player_with_biggest_shoe = max(players_with_shoes(all_players()), key=players_with_shoes(all_players()).get)
	stats_dict = player_stats(player_with_biggest_shoe)
	return stats_dict['rebounds']
    


def most_points_scored(): 
	return max(players_points(all_players()), key=players_points(all_players()).get)

def team_points(): 
	teams_points_dict = {}
	for location, team_stats in game_dict().items():
		teams_points_dict[game_dict()[location]['team_name']] = 0 
		for stats, data in team_stats.items():
			if stats == "players":
				for p, s in data.items(): 
					#import pdb; pdb.set_trace()
					teams_points_dict[game_dict()[location]['team_name']] += s['points']
	return teams_points_dict


def winning_team(): 
	return max(team_points(), key=team_points().get)

def good_practices():
  for location, team_stats in game_dict().items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
    import pdb; pdb.set_trace()
    for stats, data in team_stats.items():
        # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
        import pdb; pdb.set_trace()
        # what is 'data' at each level of the for loop block? when will we be able to iterate through a list? 
        # When would the following line of code break?
        for item in data:
            print(item)

def players_and_name_length(): 
	player_dict = {}
	for player in all_players():
		for location, team_stats in game_dict().items():
			for stats, data in team_stats.items():
				#import pdb; pdb.set_trace()
				if stats == "players":
				 	for p, s in data.items(): 
				 		player_dict[p] = len(p)
	return player_dict

def players_and_steals(): 
	player_dict = {}
	for player in all_players():
		for location, team_stats in game_dict().items():
			for stats, data in team_stats.items():
				#import pdb; pdb.set_trace()
				if stats == "players":
				 	for p, s in data.items(): 
				 		player_dict[p] = s['steals']
	return player_dict


def player_with_longest_name(): 
	return max(players_and_name_length(), key=players_and_name_length().get)

def player_with_the_most_steals(): 
	return max(players_and_steals(), key=players_and_steals().get)

def long_name_steals_a_ton(): 
	return player_with_longest_name() == player_with_the_most_steals()


#good_practices()
# player_name = "Ben Gordon"
# print(players_with_shoes(all_players()))
# print(max(players_with_shoes(all_players()), key=players_with_shoes(all_players()).get)
# )
# print(player_with_the_most_steals())
# print(player_with_longest_name())
# print(long_name_steals_a_ton())
#good_practices()
player_numbers("Charlotte Hornets")
