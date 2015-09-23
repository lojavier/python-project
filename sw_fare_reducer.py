#!/usr/bin/env python
import os
import re
import sys
import time
import MySQLdb
import smtplib
import datetime
import mechanize
from datetime import date
from HTMLParser import HTMLParser
from email.mime.text import MIMEText
from htmlentitydefs import name2codepoint

global temp
global outboundTime
global returnTime
global flightNum
global currentPrice
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
global currentDollarsPrice
global currentPointsPrice

def send_alert(notificationAddress,paidPrice,currentPrice,confirmationNum,originAirportCode,destinationAirportCode,outboundDate,outboundFlightNum):
	SMTP_SERVER = "smtp.gmail.com"
	SMTP_PORT = 587
	SMTP_USERNAME = "swfarereducer@gmail.com"
	SMTP_PASSWORD = "swfarereducer1"
	# SMTP_USERNAME = "swflightsearch@gmail.com"
	# SMTP_PASSWORD = "swflightsearch1"
	EMAIL_FROM = 'swfarereducer@gmail.com'
	EMAIL_TO = [notificationAddress]
	EMAIL_SPACE = ", "
	EMAIL_SUBJECT = "PRICE DROP ALERT!"
	DATA = "[%s->%s] [CONF#:%s] [%s->%s] [%s] [FLIGHT#%s] https://www.southwest.com/flight/change-air-reservation.html" % (paidPrice,currentPrice,confirmationNum,originAirportCode,destinationAirportCode,outboundDate,outboundFlightNum)
	try:
		msg = MIMEText(DATA)
		msg['Subject'] = EMAIL_SUBJECT
		msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
		msg['From'] = EMAIL_FROM
		mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		mail.starttls()
		mail.login(SMTP_USERNAME, SMTP_PASSWORD)
		mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
		mail.quit()
	except smtplib.SMTPException:
		print "ERROR: Unable to send email"

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global temp
		global flightNum
		global currentDollarsPrice
		global departTag
		global departTime
		global departTime24Hour
		global arriveTag
		global arriveTime
		global arriveTime24Hour
		global route
		for attr in attrs:
			if "title" in attr[0]:
				result = attr[1].split(' ', 8)
				flightNum = result[2]
				currentDollarsPrice = result[3]
				departTime = result[4]
				temp = time.strptime(departTime, "%I:%M%p")
				departTime24Hour = float(temp.tm_hour) + float(float(temp.tm_min) / 60)
				departTag = result[5]
				arriveTime = result[6]
				temp = time.strptime(arriveTime, "%I:%M%p")
				arriveTime24Hour = float(temp.tm_hour) + float(float(temp.tm_min) / 60)
				arriveTag = result[7]
				route = result[8]
				break
	def handle_data(self, data):
		global currentPointsPrice
		currentPointsPrice = data.replace(',','')

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
resultsFile = cwd+"/southwest_results.html"
responseFile = cwd+"/southwest_response.html"

db = MySQLdb.connect("127.0.0.1","root","swfarereducer","SWFAREREDUCERDB")
cursor = db.cursor()
# $sql = "SELECT UF.*,A.AIRPORT_NAME as DEPART_AIRPORT_NAME,B.AIRPORT_NAME as ARRIVE_AIRPORT_NAME FROM UPCOMING_FLIGHTS AS UF LEFT JOIN AIRPORTS as A ON A.AIRPORT_CODE=UF.DEPART_AIRPORT_CODE LEFT JOIN AIRPORTS as B ON B.AIRPORT_CODE=UF.ARRIVE_AIRPORT_CODE WHERE UF.CONFIRMATION_NUM='".$CONFIRMATION_NUM."' AND UF.FIRST_NAME='".$FIRST_NAME."' AND UF.LAST_NAME='".$LAST_NAME."' ORDER BY UF.DEPART_DATE ASC";
sql = "SELECT * FROM UPCOMING_FLIGHTS"
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		confirmationNum = row[1]
		firstName = row[2]
		lastName = row[3]
		notificationAddress = row[4]
		originAirportCode = row[5]
		# for i in range(0,len(airport_list)):
		# 	if originAirportCode in airport_list[i][0]:
		# 		originAirportName = airport_list[i][1]
		# 		break
		destinationAirportCode = row[6]
		# for i in range(0,len(airport_list)):
		# 	if destinationAirportCode in airport_list[i][0]:
		# 		destinationAirportName = airport_list[i][1]
		# 		break
		outboundDate = row[7]
		temp = datetime.datetime.strptime(outboundDate, "%m/%d/%Y")
		outboundDay = temp.strftime("%A")
		outboundDepartTime = row[8]
		temp = time.strptime(outboundDepartTime, "%I:%M %p")
		outboundDepartTime24Hour = float(temp.tm_hour) + float(float(temp.tm_min) / 60)
		outboundArriveTime = row[9]
		outboundFlightNum = row[10]
		fareLabel = row[11]
		paidPrice = row[12]
		fareType = row[13]

		br = mechanize.Browser()
		br.set_handle_robots(False)
		response = br.open("https://www.southwest.com/flight/")
		content = response.read()
		# with open(responseFile, "w") as f:
		#     f.write(content)
		br.select_form(name="buildItineraryForm")
		# br.select_form(nr=2)
		br.find_control(name="originAirport").value = [originAirportCode]
		br.find_control(name="destinationAirport").value = [destinationAirportCode]
		br.form["outboundDateString"] = outboundDate
		if(outboundDepartTime24Hour < 12):
			br.find_control(id="outboundTimeOfDay",name="outboundTimeOfDay").value = ['BEFORE_NOON']
		elif(18 >= outboundDepartTime24Hour >= 12):
			br.find_control(id="outboundTimeOfDay",name="outboundTimeOfDay").value = ['NOON_TO_6PM']
		elif(outboundDepartTime24Hour > 18):
			br.find_control(id="outboundTimeOfDay",name="outboundTimeOfDay").value = ['AFTER_6PM']
		br.find_control(id="roundTrip",name="twoWayTrip").value = ['false']
		try:
			br.find_control(name="fareType").value = ['POINTS']
		except:
			print "WARNING: Fare type selection is not accessible at the moment.\n"
		try:
			result = br.submit()
			southwest_results_string = result.read()
		except:
			print "ERROR: Could not submit information "
			continue
		# with open(resultsFile, "w") as f:
		#     f.write(southwest_results_string)

		parser = MyHTMLParser()

		# print originAirportName+" ---> "+destinationAirportName+" [ "+outboundDay+", "+outboundDate+" ]"
		for x in range(1,30):
			inputPosBeg = southwest_results_string.find("<input id=\"Out"+str(x)+"C\"")
			if(inputPosBeg != -1):
				inputPosEnd = southwest_results_string.find("/>", inputPosBeg)
				outboundFlightResult = southwest_results_string[(inputPosBeg):(inputPosEnd+2)]
				parser.feed(outboundFlightResult)

				if( (flightNum == outboundFlightNum) ):
					inputPosBeg2 = southwest_results_string.find("<label", inputPosBeg)
					inputPosEnd2 = southwest_results_string.find("</label>", inputPosBeg2)
					outboundFlightResult = southwest_results_string[(inputPosBeg2):(inputPosEnd2+8)]
					parser.feed(outboundFlightResult)

					# print "%s (%s)\t%s\t%s\t%s\t%s\t(Flight # %s)\t%s\tWanna Get Away\n" % (currentDollarsPrice,currentPointsPrice,departTime,departTag,arriveTime,arriveTag,flightNum,route)

					if( ("DOLLARS" in fareLabel) and (float(currentDollarsPrice.replace('$','')) < float(paidPrice)) ):
						send_alert(notificationAddress,"$"+paidPrice,currentDollarsPrice,confirmationNum,originAirportCode,destinationAirportCode,outboundDate,outboundFlightNum)
					elif( ("POINTS" in fareLabel) and (float(currentPointsPrice) < float(paidPrice)) ):
						send_alert(notificationAddress,paidPrice,currentPointsPrice,confirmationNum,originAirportCode,destinationAirportCode,outboundDate,outboundFlightNum)
					break
except:
	print "ERROR: Unable to fetch data"
	sys.exit()

db.close()