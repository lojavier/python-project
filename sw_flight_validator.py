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
	# def handle_starttag(self, tag, attrs):
	# 	global temp
	# 	global flightNum
	# 	global currentDollarsPrice
	# 	global departTag
	# 	global departTime
	# 	global departTime24Hour
	# 	global arriveTag
	# 	global arriveTime
	# 	global arriveTime24Hour
	# 	global route

	def handle_starttag(self, tag, attrs):
		# print "Start tag:", tag
		# for attr in attrs:
		# 	print "     attr:", attr
		if "span" in tag:
			for attr in attrs:
				if "class" in attr[0] and "travelDateTime" in attr[1]:
					print "     attr:", attr[1]
				if "class" in attr[0] and "nowrap" in attr[1]:
					print "     attr:", attr[1]
				if "class" in attr[0] and "nextDayContainer" in attr[1]:
					print "     attr:", attr[1]
		if "strong" in tag:
			print "Start tag:", tag
		if "td" in tag:
			print "Start tag:", tag
			for attr in attrs:
				if "class" in attr[0] and "flightNumber" in attr[1]:
					print "     attr:", attr[1]

	def handle_data(self, data):
		temp = data.strip()
		if temp:
			print "Data     :", data
		if "Arrive in" in data:
			print "Data     :", data
		if "Wanna Get Away" in data:
			print "Data     :", data

# # Round price up
# upcoming_trips = []
# upcoming_trips.append(['8ABYGC','Lorenzo','Javier','9252007284@vtext.com','SJC','PHX','10/02/2015','8:05PM','9:50PM','179','0','4291'])
# upcoming_trips.append(['8ABYGC','Lorenzo','Javier','9252007284@vtext.com','PHX','SJC','10/06/2015','5:40AM','7:35AM','2787','0','2989'])
# upcoming_trips.append(['HHGRHL','Lorenzo','Javier','9252007284@vtext.com','SJC','ONT','10/30/2015','8:20PM','9:30PM','2953','0','6798'])
# upcoming_trips.append(['HN9RRZ','Lorenzo','Javier','9252007284@vtext.com','LAX','SJC','11/02/2015','8:45AM','9:55AM','1147','0','3184'])
# upcoming_trips.append(['832STR','Lorenzo','Javier','9252007284@vtext.com','SJC','PHX','11/04/2015','6:35AM','9:20AM','539','0','2989'])
# upcoming_trips.append(['832STR','Lorenzo','Javier','9252007284@vtext.com','PHX','SJC','11/08/2015','8:40PM','9:35PM','1117','0','8459'])
# upcoming_trips.append(['8J9T7V','Danielle','Gonzalez','9095698490@txt.att.net','ONT','SJC','09/03/2015','6:45PM','7:50PM','3243','60','0'])
# upcoming_trips.append(['8J9T7V','Danielle','Gonzalez','9095698490@txt.att.net','SJC','ONT','09/09/2015','8:20PM','9:30PM','2953','63','0'])
# upcoming_trips.append(['H9CRR8','Giovanni','Javier','9257856233@vtext.com','OAK','ONT','10/30/2015','8:40AM','9:55AM','2751','0','3803'])
# upcoming_trips.append(['H38RR6','Giovanni','Javier','9257856233@vtext.com','LAX','OAK','11/02/2015','9:15AM','10:30AM','2906','0','3184'])
# # upcoming_trips.append(['','','','','','','','','','','',''])

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
flightNum = ""

#####################################################################
## Initiate mechanize, set parameters in form, and submit form
#####################################################################
cwd = os.getcwd()
resultsFile = cwd+"/southwest_conf_results.html"
responseFile = cwd+"/southwest_conf_response.html"
print ""

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
br.find_control(name="confirmationNumber").value = "8ABYGC"
br.find_control(name="firstName").value = "LORENZO"
br.find_control(name="lastName").value = "JAVIER"
# try:
result = br.submit()
southwest_conf_results_string = result.read()
with open(resultsFile, "w") as f:
	f.write(southwest_conf_results_string)
# except:
	# print "ERROR: Could not submit information "

parser = MyHTMLParser()
parser.feed(southwest_conf_results_string)

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