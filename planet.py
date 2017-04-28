# planet = Planet(id,resources,res_buildings,defenses,ships,facilities)
import csv
import json
import math

class Planet(object):
	def __init__(self, id, resources, res_buildings, defenses, ships, facilities):
		self.id = id
		self.resources = resources
		self.res_buildings = res_buildings
		self.defenses = defenses
		self.ships = ships
		self.facilities = facilities

		print (self.res_buildings)
		self.queue = []
		
		# self.add_to_queue()
		
	def production_rate(self,mul):
	#TODO dodac energie z elektrowni i z satelit
		metal = round(30 * self.res_buildings['metal_mine'] * math.pow(1.1,self.res_buildings['metal_mine']) * mul)
		crystal = round(20 * self.res_buildings['metal_mine'] * math.pow(1.1,self.res_buildings['metal_mine']) * mul)
		deuter = round(10 * self.res_buildings['metal_mine'] * math.pow(1.1,self.res_buildings['metal_mine']) * mul) #dodac temperature bo zle jest TODO
		return {'metal' : metal,'crystal' : crystal, 'deuter' : deuter}
		
	def transport_needed(self):
		return math.ceil((self.resources['metal'] + self.resources['crystal'] + self.resources['deuterium']) / 25000 )

	def check_storage(self):
		storage_capacity_lvl = [10000,20000,40000,75000,140000,255000,470000,865000,1590000,2920000,5355000,9820000,18005000,33005000,60510000,110925000]
		
		pass
		
	def next_lvl_cost(self,building,level):
	#TODO dodac inne budznki bo na rayie sa same ekonomicyzne
		base_res_build_cost = {
		'metal_mine'     : [[60,15,0],[1.5]],
		'crystal_mine'   : [[48,24,0],[1.6]],
		'deuterium_mine' : [[225,75,0],[1.5]],
		'solar_plant'    : [[75,30,0],[1.5]],
		'fusion_reactor' : [[900,360,180],[1.8]],
		'solar_satellite': [[0,2000,500],[1.0]],
		'metal_storage'  : [[1000,0,0],[2.0]],
		'crystal_storage': [[1000,500,0],[2.0]],
		'deuterium_tank' : [[1000,1000,0],[2.0]]			 
		}
		mul = base_res_build_cost[building][1][0]
		base_cost = base_res_build_cost[building][0]
		coef = [pow(mul,level)][0] #level - 1 bylo
		return [round(x * coef) for x in base_cost]


		
		
	def add_to_queue(self):
	#TODO policz i dodaj do kolejki budowy nastepny budynek
		x = {'metal_mine' : 0,'crystal_mine' : 0,'deuterium_mine' : 999999999}
		tobuild = ''
		while len(self.queue) < 1:
			#znajdz najtansza elektrownie (deu z offsetem na --)
			
			for building in ['metal_mine','crystal_mine']:
				# x.append( [building,sum(self.next_lvl_cost(building,self.res_buildings[building]))] )
				x[building] = sum(self.next_lvl_cost(building,self.res_buildings[building]))
				
			if self.resources['energy'] <= 0 and self.res_buildings['solar_plant'] < 15 :	
				self.queue.append('solar_plant')
			else:
				#find cheapest mine building and add to queue
				HERE HERE HERE HERE
				self.queue.append(min())
				
				
			print (self.queue)
			#dodaj do kolejki
			#znajdz kolejna troche drozsza
			# jesli koszt budynku jest wiekszy niz pojemnosc magazynu...
				#dodaj magazyn do kolejki
			# jesli projected energy cost jest na minusie
				#jesli elektrownia <15
					#dodaj elektrownie do kolejki
				# 
			return 0
			pass
		
		
	def perform_planet_check(self):
		pass
		