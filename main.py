
import os.path



from ogame import OGame
from planet import Planet
from manager import Manager




def main():




	USER = 'nickname'
	PASW = 'password'
	UNI = 'Spica'
	ogame = OGame(UNI, USER, PASW)
	mg = Manager(ogame)
	
	planet_ids = ogame.get_planet_ids()

	print('Is player logged in: %s' %str(ogame.is_logged()))

	#if is attacked:

	# else:
		#iterate over planets and do actions

	planets = []

	## If data file is empty or non existent
	## create planet object and fill them with info
	# if os.path.exists('planet_data.txt') and os.stat('planet_data.txt').st_size!=0:
		#Init data about planets and save to file
		# print ("File detected")
		# planets = mg.read_data()
	# else:
	print ("File NOT detected")
	for id in planet_ids:
		resources = ogame.get_resources(id)
		res_buildings = ogame.get_resources_buildings(id)
		defenses = ogame.get_defense(id)
		ships = ogame.get_ships(id)
		facilities = ogame.get_facilities(id)
		# research.append(ogame.get_research(id))
		planet = Planet(id,resources,res_buildings,defenses,ships,facilities)
		planets.append(planet)
	mg.save_data(planets)
		

	planets[0].add_to_queue()
	print (planets[0].queue)
	mg.build_request()

	
	
	print ('DONE')
	
main()