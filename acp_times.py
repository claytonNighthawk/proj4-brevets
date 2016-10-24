"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math as m

#upper limit on distance increments, used to calculate necessary speeds 
DISTANCES = [200, 400, 600, 1000]
MIN_MAX_SPEEDS = {200:{"min": 15, "max": 34}, 400:{"min": 15, "max": 32}, 600:{"min": 15, "max": 30},
				  1000:{"min": 11.428, "max": 28}} #last row is not reivant because there is no sanctioned brevets longer than 1000km


def dist_split(dist):
	"""
	returns a list break down of the km traveled to each control. 
	ie dist_split(666) = [200, 200, 200, 60] 
	which is the dist traveled from 0-200, from 200-400, from 400-600, and then 
	distance traveled above 600km.
	
	function does not record distance traveled over 1000km however but since 1000km is 
	the max	brevet length, any control over 1000km has to open open/close at the same time 
	as a control at exactly 1000km
	"""
	DIST_SUBS = [200, 200, 200, 400]
	dists = []
	for d in DIST_SUBS:
		if dist >= d:
			dists.append(d)
			dist -= d
		elif dist < d and dist > 0:
			dists.append(dist)
			dist -= d
		else: 
			dists.append(0)

	return dists

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
	"""
	Args:
	   control_dist_km:  number, the control distance in kilometers
	   brevet_dist_km: number, the nominal distance of the brevet in kilometers,
		   which must be one of 200, 300, 400, 600, or 1000 (the only official
		   ACP brevet distances)
	   brevet_start_time:  An ISO 8601 format date-time string indicating
		   the official start time of the brevet
	Returns:
	   An ISO 8601 format date string indicating the control open time.
	   This will be in the same time zone as the brevet start time.
	"""
	if control_dist_km > brevet_dist_km:
		dists = dist_split(brevet_dist_km)
	else:
		dists = dist_split(control_dist_km)

	#print("dists", dists)
	times = []
	for actual_dist, brev_dist in zip(dists, DISTANCES):
		# takes distance traveled in the distance legs and turns it into the min time per leg 
		if actual_dist == 0:
			continue 
		max_speed = MIN_MAX_SPEEDS[brev_dist]['max']
		#print("max_speed", max_speed)
		minute, hour = m.modf(actual_dist / max_speed)
		minute = round(minute * 60)
		time = (hour, minute)
		times.append(time)
	
	openTime = arrow.get(brevet_start_time)
	#print("open time legs", times)
	#print("starting open time", openTime)
	for hour, minute in times:
		minute = openTime.minute + minute #BUG done because minute=+minute just replaces instead of adds minutes 
		if minute >= 60:				  #crashes on minute = 60
			minute -= 60
			hour += 1
		openTime = openTime.replace(hours=+hour, minute=+minute)
		#print("updated open time", openTime)		
	return openTime.isoformat()

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
	"""
	Args:
	   control_dist_km:  number, the control distance in kilometers
	   brevet_dist_km: number, the nominal distance of the brevet in kilometers,
		   which must be one of 200, 300, 400, 600, or 1000 (the only official
		   ACP brevet distances)
	   brevet_start_time:  An ISO 8601 format date-time string indicating
		   the official start time of the brevet
	Returns:
	   An ISO 8601 format date string indicating the control close time.
	   This will be in the same time zone as the brevet start time.
	"""
	if control_dist_km > brevet_dist_km:
		dists = dist_split(brevet_dist_km)
	else:
		dists = dist_split(control_dist_km)

	#print("dists", dists)
	times = []
	for actual_dist, brev_dist in zip(dists, DISTANCES):
		# takes distance traveled in the distance legs and turns it into the min time per leg 
		if actual_dist == 0:
			continue 
		min_speed = MIN_MAX_SPEEDS[brev_dist]['min']
		#print("min_speed", min_speed)
		minute, hour = m.modf(actual_dist / min_speed)
		minute = round(minute * 60)
		time = (hour, minute)
		times.append(time)

	closeTime = arrow.get(brevet_start_time)
	#print("close time legs", times)
	#print("starting close time", closeTime)
	for hour, minute in times:
		minute = closeTime.minute + minute #BUG done because minute=+minute just replaces instead of adds minutes 
		if minute >= 60:				   #crashes on minute >= 60
			minute -= 60
			hour += 1
		closeTime = closeTime.replace(hours=+hour, minute=+minute)
		#print("updated close time", closeTime)
	
	if control_dist_km == 0:
		closeTime = closeTime.replace(hours=+1)
	return closeTime.isoformat()


