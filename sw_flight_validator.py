#!/usr/bin/env python
import os
import re
import sys
import time
# import MySQLdb
import smtplib
import datetime
import mechanize
from datetime import date
from HTMLParser import HTMLParser
from email.mime.text import MIMEText
from htmlentitydefs import name2codepoint
# http://www.blog.pythonlibrary.org/2012/06/08/python-101-how-to-submit-a-web-form/
# http://www.thetaranights.com/fill-online-form-using-python/
# http://wwwsearch.sourceforge.net/mechanize/download.html
# http://readwrite.com/2014/06/27/raspberry-pi-web-server-website-hosting
global temp
global outboundTime
global returnTime
global flightNum
global currentDollarsPrice
global currentPointsPrice
global departTag
global departTime
global departTime24Hour
global arriveTag
global arriveTime
global arriveTime24Hour
global route
global upcoming_trips
global paidPrice
global confirmationNum
global firstName
global lastName
global notificationAddress
global outboundArriveTime
global outboundFlightNum
global paidDollarsPrice
global paidPointsPrice

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global departureDateFlag
		global departureCityFlag
		global departureTimeFlag
		global arrivalCityFlag
		global arrivalTimeFlag
		global strongFlag
		global tdFlag
		if "span" in tag:
			for attr in attrs:
				if "class" in attr[0] and "travelDateTime" in attr[1]:
					departureDateFlag = True
					print "     attr:", attr[1]
				if "class" in attr[0] and "nowrap" in attr[1] and "nextDayContainer" not in attr[1]:
					departureTimeFlag = True
					print "     attr:", attr[1]
				if "class" in attr[0] and "nextDayContainer" in attr[1]:
					arrivalTimeFlag = True
					print "     attr:", attr[1]
		elif "strong" in tag:
			print "Start tag:", tag
			strongFlag = True
		elif "td" in tag:
			tdFlag = True
			print "Start tag:", tag
			for attr in attrs:
				if "class" in attr[0] and "flightNumber" in attr[1]:
					print "     attr:", attr[1]
		else:
			strongFlag = False
			tdFlag = False
	def handle_data(self, data):
		global roundTripFlag
		global departureCity1
		global departureDate1
		global departureTime1
		global departureCity2
		global departureDate2
		global departureTime2
		global departureCityFlag
		global departureDateFlag
		global departureTimeFlag
		global arrivalCity1
		global arrivalTime1
		global arrivalCity2
		global arrivalTime2
		global arrivalCityFlag
		global arrivalTimeFlag
		global flightNum1
		global flightNum2
		global flightNumFlag
		global strongFlag
		global tdFlag
		data = data.strip()
		if data:
			# Departure of 1st flight (city)
			if departureCityFlag and strongFlag and not roundTripFlag:
				departureCity1 = data
				departureCityFlag = False
				print "Data     :", data
			# Departure of 1st flight (date)
			elif departureDateFlag and tdFlag and not roundTripFlag:
				departureDate1 = data
				departureDateFlag = False
				roundTripFlag = True
				print "Data     :", data
			# Departure of 1st flight (time)
			elif departureTimeFlag and strongFlag and not roundTripFlag:
				departureTime1 = data
				departureTimeFlag = False
				print "Data     :", data
			# Arrival of 1st flight (city)
			elif arrivalCityFlag and strongFlag and not roundTripFlag:
				arrivalCity1 = data
				arrivalCityFlag = False
				print "Data     :", data
			# Arrival of 1st flight (time)
			elif arrivalTimeFlag and strongFlag and not roundTripFlag:
				arrivalTime1 = data
				arrivalTimeFlag = False
				print "Data     :", data
			# Flight number of 1st flight
			elif flightNumFlag and strongFlag and not roundTripFlag:
				flightNum1 = data.strip('#')
				flightNumFlag = False
				print "Data     :", data
			# Departure of 2nd flight (city)
			elif departureCityFlag and strongFlag and roundTripFlag:
				departureCity2 = data
				departureCityFlag = False
				print "Data     :", data
			# Departure of 2nd flight (date)
			elif departureDateFlag and tdFlag and roundTripFlag:
				departureDate2 = data
				departureDateFlag = False
				print "Data     :", data
			# Departure of 2nd flight (date)
			elif departureTimeFlag and strongFlag and roundTripFlag:
				departureTime2 = data
				departureTimeFlag = False
				print "Data     :", data
			# Arrival of 2nd flight (city)
			elif arrivalCityFlag and strongFlag and roundTripFlag:
				arrivalCity2 = data
				arrivalCityFlag = False
				print "Data     :", data
			# Arrival of 2nd flight (time)
			elif arrivalTimeFlag and strongFlag and roundTripFlag:
				arrivalTime2 = data
				arrivalTimeFlag = False
				print "Data     :", data
			# Flight number of 2nd flight
			elif flightNumFlag and strongFlag and roundTripFlag:
				flightNum2 = data.strip('#')
				flightNumFlag = False
				print "Data     :", data
			elif "Depart" in data:
				departureCityFlag = True
				print "Data     :", data
			elif "Arrive in" in data:
				arrivalCityFlag = True
				print "Data     :", data
			elif "Wanna Get Away" in data:
				print "Data     :", data
			elif "Flight" in data:
				flightNumFlag = True
				print "Data     :", data
			else:
				departureCityFlag = False
				departureDateFlag = False
				departureTimeFlag = False
				arrivalCityFlag = False
				arrivalTimeFlag = False
				flightNumFlag = False
				print "Data     :", data

airport_list = []
airport_list.append(['OAK','Oakland, CA - OAK'])
airport_list.append(['SJC','San Jose, CA - SJC'])
airport_list.append(['SFO','San Francisco, CA - SFO'])
airport_list.append(['ONT','Ontario/LA, CA - ONT'])
airport_list.append(['SNA','Orange County/Santa Ana, CA - SN'])
airport_list.append(['LAX','Los Angeles, CA - LAX'])
airport_list.append(['LAS','Las Vegas, NV - LAS'])
airport_list.append(['PHX','Phoenix, AZ - PHX'])
airport_list.append(['SAN','San Diego, CA - SAN'])
airport_list.append(['ALB','Albany, NY - ALB'])
airport_list.append(['BUF','Buffalo/Niagara, NY - BUF'])
airport_list.append(['ISP','Long Island/Islip, NY - ISP'])
airport_list.append(['LGA','New York (LaGuardia), NY - LGA'])
airport_list.append(['EWR','New York/Newark, NJ - EWR'])
airport_list.append(['ROC','Rochester, NY - ROC'])
airport_list.append(['SMF','Sacramento, CA - SMF'])
airport_list.append(['SEA','Seattle/Tacoma, WA - SEA'])

#####################################################################
## Set user input variables
#####################################################################
temp = ""
currentDollarsPrice = ""
currentPointsPrice = ""
departTag = ""
departTime = ""
arriveTag = ""
arriveTime = ""
route = ""
flightNum1 = ""
flightNum2 = ""

#####################################################################
## Initiate mechanize, set parameters in form, and submit form
#####################################################################
cwd = os.getcwd()
resultsFile = cwd+"/southwest_conf_results.html"
responseFile = cwd+"/southwest_conf_response.html"
print ""

departureDate1 = ""
departureCity1 = ""
departureTime1 = ""
departureDate2 = ""
departureCity2 = ""
departureTime2 = ""
arrivalCity1 = ""
arrivalTime1 = ""
arrivalCity2 = ""
arrivalTime2 = ""
departureDateFlag = False
departureCityFlag = False
departureTimeFlag = False
arrivalCityFlag = False
arrivalTimeFlag = False
flightNumFlag = False
strongFlag = False
tdFlag = False
roundTripFlag = False

# db = MySQLdb.connect("localhost","root","swfarereducer","SWFAREREDUCERDB")
# cursor = db.cursor()
# sql = "SELECT * FROM SWFAREREDUCERDB.UPCOMING_FLIGHTS"
# try:
# 	cursor.execute(sql)
# 	results = cursor.fetchall()
# 	for row in results:
# 		confirmationNum = row[1]
# 		firstName = row[2]
# 		lastName = row[3]
# 		notificationAddress = row[4]
# 		originAirportCode = row[5]
# 		for i in range(0,len(airport_list)):
# 			if originAirportCode in airport_list[i][0]:
# 				originAirportName = airport_list[i][1]
# 				break
# 		destinationAirportCode = row[6]
# 		for i in range(0,len(airport_list)):
# 			if destinationAirportCode in airport_list[i][0]:
# 				destinationAirportName = airport_list[i][1]
# 				break
# 		outboundDate = row[7]
# 		temp = datetime.datetime.strptime(outboundDate, "%m/%d/%Y")
# 		outboundDay = temp.strftime("%A")
# 		outboundDepartTime = row[8]
# 		temp = time.strptime(outboundDepartTime, "%I:%M%p")
# 		outboundDepartTime24Hour = float(temp.tm_hour) + float(float(temp.tm_min) / 60)
# 		outboundArriveTime = row[9]
# 		outboundFlightNum = row[10]
# 		paidDollarsPrice = row[11]
# 		paidPointsPrice = row[12]

# 		br = mechanize.Browser()
# 		br.set_handle_robots(False)
# 		response = br.open("https://www.southwest.com/flight/")
# 		content = response.read()
# 		with open(responseFile, "w") as f:
# 		    f.write(content)
# 		br.select_form(name="buildItineraryForm")
# 		# br.select_form(nr=2)
# 		br.find_control(name="originAirport").value = [originAirportCode]
# 		br.find_control(name="destinationAirport").value = [destinationAirportCode]
# 		br.form["outboundDateString"] = outboundDate
# 		if(outboundDepartTime24Hour < 12):
# 			br.find_control(id="outboundTimeOfDay",name="outboundTimeOfDay").value = ['BEFORE_NOON']
# 		elif(18 >= outboundDepartTime24Hour <= 12):
# 			br.find_control(id="outboundTimeOfDay",name="outboundTimeOfDay").value = ['NOON_TO_6PM']
# 		elif(outboundDepartTime24Hour > 18):
# 			br.find_control(id="outboundTimeOfDay",name="outboundTimeOfDay").value = ['AFTER_6PM']
# 		br.find_control(id="roundTrip",name="twoWayTrip").value = ['false']
# 		try:
# 			br.find_control(name="fareType").value = ['POINTS']
# 		except:
# 			print "WARNING: Fare type selection is not accessible at the moment.\n"
# 		try:
# 			result = br.submit()
# 		except:
# 			print "ERROR: Could not submit information "
# 			continue
# 		southwest_results_string = result.read()
# 		with open(resultsFile, "w") as f:
# 		    f.write(southwest_results_string)

# 		parser = MyHTMLParser()

# 		print originAirportName+" ---> "+destinationAirportName+" [ "+outboundDay+", "+outboundDate+" ]"
# 		for x in range(1,30):
# 			inputPosBeg = southwest_results_string.find("<input id=\"Out"+str(x)+"C\"")
# 			if(inputPosBeg != -1):
# 				inputPosEnd = southwest_results_string.find("/>", inputPosBeg)
# 				outboundFlightResult = southwest_results_string[(inputPosBeg):(inputPosEnd+2)]
# 				parser.feed(outboundFlightResult)

# 				if( (flightNum == outboundFlightNum) ):
# 					inputPosBeg2 = southwest_results_string.find("<label", inputPosBeg)
# 					inputPosEnd2 = southwest_results_string.find("</label>", inputPosBeg2)
# 					outboundFlightResult = southwest_results_string[(inputPosBeg2):(inputPosEnd2+8)]
# 					parser.feed(outboundFlightResult)

# 					print "%s (%s)\t%s\t%s\t%s\t%s\t(Flight # %s)\t%s\n" % (currentDollarsPrice,currentPointsPrice,departTime,departTag,arriveTime,arriveTag,flightNum,route)
					
# 					if( float(currentDollarsPrice.replace('$','')) < float(paidDollarsPrice) ):
# 						send_alert(notificationAddress,"$"+paidDollarsPrice,currentDollarsPrice,confirmationNum,originAirportCode,destinationAirportCode,outboundDate,outboundFlightNum)
# 					elif( float(currentPointsPrice) < float(paidPointsPrice) ):
# 						send_alert(notificationAddress,paidPointsPrice,currentPointsPrice,confirmationNum,originAirportCode,destinationAirportCode,outboundDate,outboundFlightNum)
# 					break
# except:
# 	print "ERROR: Unable to fetch data"
# 	sys.exit()

# db.close()

# for x in range(0,len(upcoming_trips)):
# 	confirmationNum = upcoming_trips[x][0]
# 	firstName = upcoming_trips[x][1]
# 	lastName = upcoming_trips[x][2]
# 	notificationAddress = upcoming_trips[x][3]
# 	originAirportCode = upcoming_trips[x][4]
# 	for i in range(0,len(airport_list)):
# 		if originAirportCode in airport_list[i][0]:
# 			originAirportName = airport_list[i][1]
# 			break
# 	destinationAirportCode = upcoming_trips[x][5]
# 	for i in range(0,len(airport_list)):
# 		if destinationAirportCode in airport_list[i][0]:
# 			destinationAirportName = airport_list[i][1]
# 			break
# 	outboundDate = upcoming_trips[x][6]
# 	temp = datetime.datetime.strptime(outboundDate, "%m/%d/%Y")
# 	outboundDay = temp.strftime("%A")
# 	outboundDepartTime = upcoming_trips[x][7]
# 	temp = time.strptime(outboundDepartTime, "%I:%M%p")
# 	outboundDepartTime24Hour = float(temp.tm_hour) + float(float(temp.tm_min) / 60)
# 	outboundArriveTime = upcoming_trips[x][8]
# 	outboundFlightNum = upcoming_trips[x][9]
# 	paidDollarsPrice = upcoming_trips[x][10]
# 	paidPointsPrice = upcoming_trips[x][11]

br = mechanize.Browser()
br.set_handle_robots(False)
response = br.open("https://www.southwest.com/flight/change-air-reservation.html")
content = response.read()
with open(responseFile, "w") as f:
    f.write(content)
br.select_form(predicate=lambda f: f.attrs.get('id', None) == 'reservationLookupCriteria')
br.find_control(name="confirmationNumber").value = "8ABYGC" # "HN9RRZ"
br.find_control(name="firstName").value = "LORENZO"
br.find_control(name="lastName").value = "JAVIER"
# try:
result = br.submit()
southwest_conf_results_string = result.read()
with open(resultsFile, "w") as f:
	f.write(southwest_conf_results_string)
# except:
	# print "ERROR: Could not submit information "

with open(resultsFile, "r") as f:
	southwest_conf_results_string = f.read()
parser = MyHTMLParser()
parser.feed(southwest_conf_results_string)

print "Departure City: " + departureCity1
print "Arrival City  : " + arrivalCity1
print "Departure Date: " + departureDate1
print "Departure Time: " + departureTime1
print "Arrival Time  : " + arrivalTime1
print "Flight #      : " + flightNum1

print "Departure City: " + departureCity2
print "Arrival City  : " + arrivalCity2
print "Departure Date: " + departureDate2
print "Departure Time: " + departureTime2
print "Arrival Time  : " + arrivalTime2
print "Flight #      : " + flightNum2

# 	print originAirportName+" ---> "+destinationAirportName+" [ "+outboundDay+", "+outboundDate+" ]"
# 	for x in range(1,30):
# 		inputPosBeg = southwest_results_string.find("<input id=\"Out"+str(x)+"C\"")
# 		if(inputPosBeg != -1):
# 			inputPosEnd = southwest_results_string.find("/>", inputPosBeg)
# 			outboundFlightResult = southwest_results_string[(inputPosBeg):(inputPosEnd+2)]
# 			parser.feed(outboundFlightResult)

# 			if( (flightNum == outboundFlightNum) ):
# 				inputPosBeg2 = southwest_results_string.find("<label", inputPosBeg)
# 				inputPosEnd2 = southwest_results_string.find("</label>", inputPosBeg2)
# 				outboundFlightResult = southwest_results_string[(inputPosBeg2):(inputPosEnd2+8)]
# 				parser.feed(outboundFlightResult)

# 				print "%s (%s)\t%s\t%s\t%s\t%s\t(Flight # %s)\t%s\n" % (currentDollarsPrice,currentPointsPrice,departTime,departTag,arriveTime,arriveTag,flightNum,route)
				
# 				if( float(currentDollarsPrice.replace('$','')) < float(paidDollarsPrice) ):
# 					send_alert(notificationAddress,"$"+paidDollarsPrice,currentDollarsPrice,confirmationNum,originAirportCode,destinationAirportCode,outboundDate,outboundFlightNum)
# 				elif( float(currentPointsPrice) < float(paidPointsPrice) ):
# 					send_alert(notificationAddress,paidPointsPrice,currentPointsPrice,confirmationNum,originAirportCode,destinationAirportCode,outboundDate,outboundFlightNum)
# 				break