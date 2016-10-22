"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math as m

DISTANCES = [200, 400, 600, 1000]
MIN_MAX_SPEEDS = {200:{"min": 15, "max": 34}, 400:{"min": 15, "max": 32},
				  600:{"min": 11.428, "max": 28}, 1000:{"min": 13.333 , "max": 26}, }

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#
def dist_split(dist):
	#returns a list break down of the km traveled to each control. 
	#ie dist_split(666) = [200, 200, 200, 60] 
	#the dist traveled from 0-200, from 200-400, from 400-600, and from 6 traveled after 600km
  DIST_SUBS = [200, 200, 200, 400]
  dists = []
  for d in DIST_SUBS:
	if dist > d:
	  dists.append(d)
	  dist -= d
	elif dist < d and dist > 0:
	  dists.append(dist)
	  dist -= d
	else: 
	  dists.append(0)

  return dists

def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
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
	brevet_start_time = arrow.get(brevet_start_time)
	if control_dist_km > brevet_dist_km:
		dists = dist_split(brevet_dist_km)
	else:
		dists = dist_split(control_dist_km)

	times = []
	for a_dist, b_dist in zip(dists, DISTANCES):
		max_speed = MIN_MAX_SPEEDS[b_dist]['max']
		time = a_dist / max_speed
		times.append(m.ceil(time))

	openTime = brevet_start_time.replace(hours=+sum(times))
	return 

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
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
		...
	else:
		...
	return arrow.now().isoformat()


