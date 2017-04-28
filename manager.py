import time
import json

from planet import Planet
from ogame import *

class Manager(OGame):
	def __init__(self,ogame):
		self.planets = []
		self.ogame = ogame
		
	def save_data(self,planets):
		with open('planet_data.txt', 'w') as f:
			data = [' '.join(['Entry created: ',str(time.strftime("%d/%m/%Y")),' ',str(time.strftime("%H:%M:%S")) ])]
			for planet in planets:
				planet_data = []
				for item in [planet.id,planet.resources,planet.res_buildings,planet.defenses,planet.ships,planet.facilities]:
					planet_data.append(json.dumps(item))
				data.append('\n'.join(planet_data))
			data.append('\n')
			f.write('\n\n'.join(data))
		self.planets = planets
			
			
	def read_data(self):
	#TODO
		with open('planet_data.txt', 'r') as f:
			fcontent = f.read().splitlines()	
			data = fcontent[0]
			
			planet_data = []
			
			for line in fcontent[2:-1]:
				if line and len(planet_data) <= 6:
					planet_data.append(json.loads(line))
				else:
					# self.planets.append(planet_data)
					# print (planet_data)
					self.planets.append(Planet(planet_data[0],planet_data[1],planet_data[2],planet_data[3],planet_data[4],planet_data[5]))
					planet_data = []
			
			return self.planets
		
	def calc_build_time(self):
		pass
		

	def build_request(self):
		Buildings = {
			 'metal_mine': 1,
             'crystal_mine': 2,
             'deuterium_mine': 3,
             'solar_plant': 4,
             'fusion_reactor': 12,
             'metal_storage': 22,
             'crystal_storage': 23,
             'deuterium_tank': 24,
			}
		# print ("lolololo")
		# print (self.planets)
		for planet in self.planets:
			if planet.queue[0] != None:
				# print (Buildings[planet.queue[0][0]])
				self.ogame.build_building(planet.id, Buildings[planet.queue[0][0]])
		print ('jobs done')
			
			
		pass
	
			# print(fcontent)
			
	# base_res_build_cost = {
		# 'metal_mine'     : [[60,15,0],[1.5]],
		# 'crystal_mine'   : [[48,24,0],[1.6]],
		# 'deuterium_mine' : [[225,75,0],[1.5]],
		# 'solar_plant'    : [[75,30,0],[1.5]],
		# 'fusion_reactor' : [[900,360,180],[1.8]],
		# 'solar_satellite': [[0,2000,500],[1.0]],
		# 'metal_storage'  : [[1000,0,0],[2.0]],
		# 'crystal_storage': [[1000,500,0],[2.0]],
		# 'deuterium_tank' : [[1000,1000,0],[2.0]]			 
	# }

	# base_facility_cost = {
			# 'robotics_factory' : [[400,120,200],[2.0]],
			# 'shipyard'         : [[400,200,100],[2.0]],
			# 'research_lab'	   : [[200,400,200],[2.0]],
			# 'alliance_depot'   : [[20000,40000,0],[2.0]],
			# 'missile_silo'     : [[20000,20000,1000],[2.0]],
			# 'nanite_factory'   : [[1000000,500000,100000],[2.0]],
			# 'terraformer'      : [[0,50000,100000],[2.0]],
			# 'space_dock'       : [[200,0,50],[2.0]]			 
	# }
	
	# storage_capacity_lvl = [10000,20000,40000,75000,140000,255000,470000,865000,1590000,2920000,5355000,9820000,18005000,33005000,60510000,110925000]
	
	base_production = {
		
	}