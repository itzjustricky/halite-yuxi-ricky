import hlt
def dock_planet(map_history):

	# the original comment queue
	command_queue=[]

	# get the current map status	
	current_map = map_history[-1]

	# get my id
	my_id = current_map.get_me()	

	# get the my ships status
	my_ships = my_id.all_ships()

	# get the planet info
	planets = current_map.all_planets()

	# filter out the ships that are not docked
	undocked_my_ships = [x for x in my_ships if x.docking_status != x.DockingStatus.UNDOCKED]

	# filter out the unoccupied planets
	unoccupied_planets= [x for x in planets if not x.is_owned()]
	

	for ship in my_ships:
		if len(unoccupied_planets) != 0:
			planet_distance = [ship.calculate_distance_between(x) for x in unoccupied_planets]

			closest_planet = planet_distance.index(min(planet_distance))
			target_planet = unoccupied_planets[closest_planet]
			del unoccupied_planets[closest_planet]
			if ship.can_dock(target_planet):
				command_queue.append(ship.dock(target_planet))
			else:
				navigate_command = ship.navigate(ship.closest_point_to(target_planet), current_map, speed=int(hlt.constants.MAX_SPEED),ignore_ships=True)
				if navigate_command:
					command_queue.append(navigate_command)
	
	return command_queue

