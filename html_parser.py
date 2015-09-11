#!/usr/bin/env python
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		global output
		if "option" in tag:
			for attr in attrs:
				if "value" in attr[0]:
					# print "     attr:", attr[1]
					output += "(\'%s\',\'" % (attr[1])
	def handle_data(self, data):
		global output
		# print "Data     :", data
		output += "%s\'),\n" % (data)

string="<option value='CAK'>Akron-Canton, OH - CAK</option><option value='ALB'>Albany, NY - ALB</option><option value='ABQ'>Albuquerque, NM - ABQ</option><option value='AMA'>Amarillo, TX - AMA</option><option value='AUA'>Aruba, Aruba - AUA</option><option value='ATL'>Atlanta, GA - ATL</option><option value='AUS'>Austin, TX - AUS</option><option value='BWI'>Baltimore/Washington, MD - BWI</option><option value='BZE'>Belize City, Belize - BZE</option><option value='BHM'>Birmingham, AL - BHM</option><option value='BOI'>Boise, ID - BOI</option><option value='BOT' class='cityArea'>[Boston Area:]</option><option value='BOS' class='inCityArea'>&nbsp;&nbsp;Boston Logan, MA - BOS</option><option value='MHT' class='inCityArea'>&nbsp;&nbsp;Manchester, NH - MHT</option><option value='PVD' class='inCityArea'>&nbsp;&nbsp;Providence, RI - PVD</option><option value='BOS'>Boston Logan, MA - BOS</option><option value='BUF'>Buffalo/Niagara, NY - BUF</option><option value='BUR'>Burbank, CA - BUR</option><option value='SJD'>Cabo San Lucas/Los Cabos, MX - SJD</option><option value='CUN'>Cancun, Mexico - CUN</option><option value='CHS'>Charleston, SC - CHS</option><option value='CLT'>Charlotte, NC - CLT</option><option value='MDW'>Chicago (Midway), IL - MDW</option><option value='CNN' class='cityArea'>[Cincinnati Area:]</option><option value='DAY' class='inCityArea'>&nbsp;&nbsp;Dayton, OH - DAY</option><option value='CLE'>Cleveland, OH - CLE</option><option value='CVL' class='cityArea'>[Cleveland Area:]</option><option value='CAK' class='inCityArea'>&nbsp;&nbsp;Akron-Canton, OH - CAK</option><option value='CLE' class='inCityArea'>&nbsp;&nbsp;Cleveland, OH - CLE</option><option value='CMH'>Columbus, OH - CMH</option><option value='CRP'>Corpus Christi, TX - CRP</option><option value='DAL'>Dallas (Love Field), TX - DAL</option><option value='DAY'>Dayton, OH - DAY</option><option value='DEN'>Denver, CO - DEN</option><option value='DSM'>Des Moines, IA - DSM</option><option value='DTW'>Detroit, MI - DTW</option><option value='ELP'>El Paso, TX - ELP</option><option value='FNT'>Flint, MI - FNT</option><option value='FLL'>Ft. Lauderdale, FL - FLL</option><option value='RSW'>Ft. Myers, FL - RSW</option><option value='GRR'>Grand Rapids, MI - GRR</option><option value='GSP'>Greenville/Spartanburg, SC - GSP</option><option value='HRL'>Harlingen, TX - HRL</option><option value='BDL'>Hartford, CT - BDL</option><option value='HOU'>Houston (Hobby), TX - HOU</option><option value='IND'>Indianapolis, IN - IND</option><option value='JAX'>Jacksonville, FL - JAX</option><option value='MCI'>Kansas City, MO - MCI</option><option value='LAS'>Las Vegas, NV - LAS</option><option value='LIR'>Liberia, Costa Rica - LIR</option><option value='LIT'>Little Rock, AR - LIT</option><option value='ISP'>Long Island/Islip, NY - ISP</option><option value='LAX'>Los Angeles, CA - LAX</option><option value='LOS' class='cityArea'>[Los Angeles Area:]</option><option value='BUR' class='inCityArea'>&nbsp;&nbsp;Burbank, CA - BUR</option><option value='LAX' class='inCityArea'>&nbsp;&nbsp;Los Angeles, CA - LAX</option><option value='ONT' class='inCityArea'>&nbsp;&nbsp;Ontario/LA, CA - ONT</option><option value='SNA' class='inCityArea'>&nbsp;&nbsp;Orange County/Santa Ana, CA - SNA</option><option value='SDF'>Louisville, KY - SDF</option><option value='LBB'>Lubbock, TX - LBB</option><option value='MHT'>Manchester, NH - MHT</option><option value='MEM'>Memphis, TN - MEM</option><option value='MEX'>Mexico City, Mexico - MEX</option><option value='MMA' class='cityArea'>[Miami Area:]</option><option value='FLL' class='inCityArea'>&nbsp;&nbsp;Ft. Lauderdale, FL - FLL</option><option value='MAF'>Midland/Odessa, TX - MAF</option><option value='MKE'>Milwaukee, WI - MKE</option><option value='MSP'>Minneapolis/St. Paul (Terminal 2), MN - MSP</option><option value='MBJ'>Montego Bay, Jamaica - MBJ</option><option value='BNA'>Nashville, TN - BNA</option><option value='NAS'>Nassau, Bahamas - NAS</option><option value='MSY'>New Orleans, LA - MSY</option><option value='NWY' class='cityArea'>[New York Area:]</option><option value='ISP' class='inCityArea'>&nbsp;&nbsp;Long Island/Islip, NY - ISP</option><option value='LGA' class='inCityArea'>&nbsp;&nbsp;New York (LaGuardia), NY - LGA</option><option value='EWR' class='inCityArea'>&nbsp;&nbsp;New York/Newark, NJ - EWR</option><option value='LGA'>New York (LaGuardia), NY - LGA</option><option value='EWR'>New York/Newark, NJ - EWR</option><option value='ORF'>Norfolk, VA - ORF</option><option value='NFB' class='cityArea'>[Northwest Florida Beaches Area:]</option><option value='ECP' class='inCityArea'>&nbsp;&nbsp;Panama City Beach, FL - ECP</option><option value='PNS' class='inCityArea'>&nbsp;&nbsp;Pensacola, FL - PNS</option><option value='OAK'>Oakland, CA - OAK</option><option value='OKC'>Oklahoma City, OK - OKC</option><option value='OMA'>Omaha, NE - OMA</option><option value='ONT'>Ontario/LA, CA - ONT</option><option value='SNA'>Orange County/Santa Ana, CA - SNA</option><option value='MCO'>Orlando, FL - MCO</option><option value='ECP'>Panama City Beach, FL - ECP</option><option value='PNS'>Pensacola, FL - PNS</option><option value='PHL'>Philadelphia, PA - PHL</option><option value='PHX'>Phoenix, AZ - PHX</option><option value='PIT'>Pittsburgh, PA - PIT</option><option value='PDX'>Portland, OR - PDX</option><option value='PWM'>Portland, ME - PWM</option><option value='PVD'>Providence, RI - PVD</option><option value='PVR'>Puerto Vallarta, MX - PVR</option><option value='PUJ'>Punta Cana, DR - PUJ</option><option value='RDU'>Raleigh/Durham, NC - RDU</option><option value='RNO'>Reno/Tahoe, NV - RNO</option><option value='RIC'>Richmond, VA - RIC</option><option value='ROC'>Rochester, NY - ROC</option><option value='SMF'>Sacramento, CA - SMF</option><option value='SLC'>Salt Lake City, UT - SLC</option><option value='SAT'>San Antonio, TX - SAT</option><option value='SAN'>San Diego, CA - SAN</option><option value='SFO'>San Francisco, CA - SFO</option><option value='SFC' class='cityArea'>[San Francisco Area:]</option><option value='OAK' class='inCityArea'>&nbsp;&nbsp;Oakland, CA - OAK</option><option value='SFO' class='inCityArea'>&nbsp;&nbsp;San Francisco, CA - SFO</option><option value='SJC' class='inCityArea'>&nbsp;&nbsp;San Jose, CA - SJC</option><option value='SJC'>San Jose, CA - SJC</option><option value='SJO'>San Jose, Costa Rica - SJO</option><option value='SJU'>San Juan, PR - SJU</option><option value='SEA'>Seattle/Tacoma, WA - SEA</option><option value='GEG'>Spokane, WA - GEG</option><option value='STL'>St. Louis, MO - STL</option><option value='TPA'>Tampa, FL - TPA</option><option value='TUS'>Tucson, AZ - TUS</option><option value='TUL'>Tulsa, OK - TUL</option><option value='IAD'>Washington (Dulles), DC - IAD</option><option value='DCA'>Washington (Reagan National), DC - DCA</option><option value='WDC' class='cityArea'>[Washington, D.C. Area:]</option><option value='BWI' class='inCityArea'>&nbsp;&nbsp;Baltimore/Washington, MD - BWI</option><option value='IAD' class='inCityArea'>&nbsp;&nbsp;Washington (Dulles), DC - IAD</option><option value='DCA' class='inCityArea'>&nbsp;&nbsp;Washington (Reagan National), DC - DCA</option><option value='PBI'>West Palm Beach, FL - PBI</option><option value='ICT'>Wichita, KS - ICT</option>"

output = ""

parser = MyHTMLParser()
parser.feed(string)

print output