from __future__ import print_function
import tracker_funcs as t
import json, datetime, copy
import Pysolar.constants as c
from constants import constants as x

preTime = datetime.datetime(x.sYear, x.sMonth, x.sDay, 4, 18, 34) #tzinfo = datetime.timezone.utc)
postTime = datetime.datetime(x.sYear, x.sMonth, x.sDay, 11, 18, 34) #tzinfo = datetime.timezone.utc)

#SunRISE calculation
start = t.calcSunriseTime(x.sLat, x.sLon, preTime)
print ("Sunrise (UTC) time is: ", start)
print("SUNRISE_starttime: ", start, " ", t.localToUTC(start, -7))

#SunSET calculation
stop = t.calcSunsetTime(x.sLat, x.sLon, postTime)
print("sunset_time: ", stop)


#Location Object Initializing
print ("Demoing: ", x.sName)
demoLoc = t.Location(x.sName, x.sLat, x.sLon, start, x.distAO1, x.distAO2)


# print ("Input time (", x.sZone, ")", preTime.strftime('%H:%M:%S'))
# preTime += datetime.timedelta(hours = -x.sOffset) #Converted inputted (PST) --> UTC standard (+7 hrs)
# print ("Input time (UTC): ", preTime.strftime('%H:%M:%S'))


#Simulate the day
demoLoc.simulateDemoDay(x.sLat, x.sLon, x.sOffset, x.sZone, start, stop)