import math
def do_turn(pw):

	boolean = 0
	dest = 0
	if (len(pw.my_planets()) == 0 or len(pw.my_fleets()) >= 1):
		return
	if len(pw.neutral_planets()) >= 1 and len(pw.my_planets()) < 9:
		planets = pw.neutral_planets()
		dest = planets[0]
		dest = closest_planet(planets, pw.my_planets()[0], dest)
		planets = pw.enemy_planets()
		dst = planets[0]
		dst = closest_planet(planets, pw.my_planets()[0], dst)
		if distance(dst.x(),dst.y(), pw.my_planets()[0].x(), pw.my_planets()[0].y()) < distance(dest.x(),dest.y(), pw.my_planets()[0].x(), pw.my_planets()[0].y()):
			dest = dst
			boolean = 1
	else:
		if len(pw.enemy_planets()) >= 1:
			enemy = pw.enemy_planets()
			dest = pw.enemy_planets()[0]
			dest = closest_planet(enemy, pw.my_planets()[0],dest)
			boolean = 1
	source = pw.my_planets()[0]
	if len(pw.enemy_planets()) == 0:
		return
	num_ships = source.num_ships() / 2
	if boolean == 0:
		my_planets = pw.my_planets()
		most_fleets = my_planets[0].num_ships()
		for i in range(1,len(my_planets)):
			if my_planets[i].num_ships() > most_fleets:
				most_fleets = my_planets[i].num_ships()
				source = my_planets[i]
		if dest.num_ships() + 1 < most_fleets:
			num_ships = dest.num_ships() + 1
		else:
			num_ships = most_fleets / 2
	else:
		source = min_amount_fleets(pw,dest)
		if (dest.num_ships() + (pw.distance(source, dest) * dest.growth_rate()) + 1 < source.num_ships()):
			num_ships = dest.num_ships() + 1 + (pw.distance(source, dest) * dest.growth_rate())
		else:
			my_planets = pw.my_planets()
			most_fleets = my_planets[0].num_ships()
			for i in range(1,len(my_planets)):
				if my_planets[i].num_ships() > most_fleets:
					most_fleets = my_planets[i].num_ships()
					source = my_planets[i]
			if (dest.num_ships() + (pw.distance(source, dest) * dest.growth_rate()) + 1 < source.num_ships()):
				num_ships = dest.num_ships() + 1 + (pw.distance(source, dest) * dest.growth_rate())
			else:
				num_ships = most_fleets / 2
	
	pw.debug('Num Ships: ' + str(num_ships) + "Bool = " + str(boolean))
	
	
	pw.issue_order(source, dest, num_ships)
def closest_planet(planets, src, dst):
	closest_dist = distance(src.x(),src.y(),dst.x(),dst.y())
	for i in range(1,len(planets)):
			x = planets[i].x()
			y = planets[i].y()
			if distance(src.x(),src.y(),x,y) < closest_dist:
				closest_dist = distance(src.x(),src.y(),x,y)
				dst = planets[i]
	return dst
def min_amount_fleets(pw,dst):
	src = pw.my_planets()[0]
	planets = pw.my_planets()
	closest_dist = pw.distance(src,dst)
	for i in range(1,len(planets)):
			if pw.distance(planets[i],dst) < closest_dist:
				closest_dist = pw.distance(src,planets[i])
				src = planets[i]
	return src
def distance(p0x, p0y, p1x, p1y):
    return math.sqrt((p0x - p1x)**2 + (p0y - p1y)**2)
	
