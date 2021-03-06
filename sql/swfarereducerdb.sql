DROP DATABASE SWFAREREDUCERDB;

START TRANSACTION;

/* ******************************** CREATE DATABASE ******************************** */

CREATE DATABASE IF NOT EXISTS SWFAREREDUCERDB
CHARACTER SET utf8 COLLATE utf8_general_ci;

/* ****************************************************************************** */
/* ******************************** CREATE TABLE ******************************** */

CREATE TABLE IF NOT EXISTS SWFAREREDUCERDB.UPCOMING_FLIGHTS (
UPCOMING_FLIGHT_ID			INT(11) NOT NULL AUTO_INCREMENT,
CONFIRMATION_NUM			VARCHAR(6) NOT NULL,
FIRST_NAME					VARCHAR(255) NOT NULL,
LAST_NAME					  VARCHAR(255) NOT NULL,
EMAIL						    VARCHAR(255) NOT NULL,
DEPART_AIRPORT_CODE VARCHAR(3) DEFAULT NULL,
ARRIVE_AIRPORT_CODE	VARCHAR(3) DEFAULT NULL,
DEPART_DATE					DATE, #VARCHAR(10) DEFAULT NULL, 
DEPART_TIME					TIME, #VARCHAR(8) DEFAULT NULL,
ARRIVE_TIME					TIME, #VARCHAR(8) DEFAULT NULL,
FLIGHT_NUM					VARCHAR(9) DEFAULT NULL,
FARE_LABEL					VARCHAR(7) NOT NULL DEFAULT 'DOLLARS',
FARE_PRICE					INT(10) NOT NULL DEFAULT 0,
FARE_TYPE					  VARCHAR(15) NOT NULL DEFAULT 'Wanna Get Away',
LAST_ALERT					TIMESTAMP NULL,
SUBMISSION_DATE			TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (UPCOMING_FLIGHT_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='UPCOMING FLIGHTS' AUTO_INCREMENT=100000;

CREATE TABLE IF NOT EXISTS SWFAREREDUCERDB.AIRPORTS (
AIRPORT_ID			INT(11) NOT NULL AUTO_INCREMENT,
AIRPORT_CODE 		VARCHAR(255) NOT NULL,
AIRPORT_NAME		VARCHAR(255) NOT NULL,
PRIMARY KEY (AIRPORT_ID),
UNIQUE (AIRPORT_CODE)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='AIRPORTS' AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS SWFAREREDUCERDB.WIRELESS_CARRIERS (
WIRELESS_CARRIER_ID		INT(11) NOT NULL AUTO_INCREMENT,
CARRIER_NAME			VARCHAR(255) NOT NULL,
CARRIER_TEXT_EMAIL		VARCHAR(255) NOT NULL,
PRIMARY KEY (WIRELESS_CARRIER_ID),
UNIQUE (CARRIER_NAME)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='WIRELESS CARRIERS' AUTO_INCREMENT=1;

/* ***************************************************************************** */
/* ******************************** INSERT INTO ******************************** */

INSERT INTO SWFAREREDUCERDB.UPCOMING_FLIGHTS (CONFIRMATION_NUM,FIRST_NAME,LAST_NAME,EMAIL,DEPART_AIRPORT_CODE,ARRIVE_AIRPORT_CODE,DEPART_DATE,DEPART_TIME,ARRIVE_TIME,FLIGHT_NUM,FARE_LABEL,FARE_PRICE,FARE_TYPE) VALUES 
('8ABYGC','Lorenzo','Javier','9252007284@vtext.com','SJC','PHX','2015-10-02','20:05','21:50','179','POINTS','4291','Wanna Get Away'),
('8ABYGC','Lorenzo','Javier','9252007284@vtext.com','PHX','SJC','2015-10-06','5:40','7:35','2787','POINTS','2989','Wanna Get Away'),
('HHGRHL','Lorenzo','Javier','9252007284@vtext.com','SJC','ONT','2015-10-30','20:20','21:30','2953','POINTS','6798','Wanna Get Away'),
('HN9RRZ','Lorenzo','Javier','9252007284@vtext.com','LAX','SJC','2015-11-02','8:45','9:55','1147','POINTS','2924','Wanna Get Away'),
('832STR','Lorenzo','Javier','9252007284@vtext.com','SJC','PHX','2015-11-03','20:10','22:50','2037','POINTS','3249','Wanna Get Away'),
('832STR','Lorenzo','Javier','9252007284@vtext.com','PHX','SJC','2015-11-08','20:40','21:35','1117','POINTS','8459','Wanna Get Away'),
('H9CRR8','Giovanni','Javier','9257856233@vtext.com','OAK','ONT','2015-10-30','8:40','9:55','2751','POINTS','3542','Wanna Get Away'),
('H38RR6','Giovanni','Javier','9257856233@vtext.com','LAX','OAK','2015-11-02','9:15','10:30','2906','POINTS','2924','Wanna Get Away'),
('HAJQGP','Danielle','Gonzalez','9095698490@txt.att.net','SJC','ONT','2015-10-30','8:35','9:45','2597','DOLLARS','73','Wanna Get Away'),
('HAJQGP','Danielle','Gonzalez','9095698490@txt.att.net','ONT','SJC','2015-11-02','19:50','21:00','103','DOLLARS','60','Wanna Get Away');
-- INSERT INTO SWFAREREDUCERDB.UPCOMING_FLIGHTS (CONFIRMATION_NUM,FIRST_NAME,LAST_NAME,EMAIL,ORIGIN_AIRPORT_CODE,DESTINATION_AIRPORT_CODE,DEPART_DATE,DEPART_TIME,ARRIVE_DATE,FLIGHT_NUM,PAID_DOLLARS,PAID_POINTS) VALUES ();

INSERT INTO SWFAREREDUCERDB.WIRELESS_CARRIERS (CARRIER_NAME,CARRIER_TEXT_EMAIL) VALUES
('Alltel','@message.alltel.com'),
('AT&T','@txt.att.net'),
('Boost Mobile','@myboostmobile.com'),
('Cricket Wireless','@sms.mycricket.com'),
('MetroPCS','@MyMetroPcs.com'),
('Nextel','@messaging.nextel.com'),
('Sprint','@messaging.sprintpcs.com'),
('T-Mobile','@tmomail.net'),
('Ting','@message.ting.com'),
('U.S. Cellular','@email.uscc.net'),
('Verizon Wireless','@vtext.com'),
('Virgin Mobile','@vmobl.com');

INSERT INTO SWFAREREDUCERDB.AIRPORTS (AIRPORT_CODE,AIRPORT_NAME) VALUES
('ALB','Albany, NY - ALB'),
('ABQ','Albuquerque, NM - ABQ'),
('AMA','Amarillo, TX - AMA'),
('AUA','Aruba, Aruba - AUA'),
('ATL','Atlanta, GA - ATL'),
('AUS','Austin, TX - AUS'),
('BZE','Belize City, Belize - BZE'),
('BHM','Birmingham, AL - BHM'),
('BOI','Boise, ID - BOI'),
('BOS','Boston Logan, MA - BOS'),
('BUF','Buffalo/Niagara, NY - BUF'),
('SJD','Cabo San Lucas/Los Cabos, MX - SJD'),
('CUN','Cancun, Mexico - CUN'),
('CHS','Charleston, SC - CHS'),
('CLT','Charlotte, NC - CLT'),
('MDW','Chicago (Midway), IL - MDW'),
('CAK','Akron-Canton, OH - CAK'),
('CLE','Cleveland, OH - CLE'),
('CMH','Columbus, OH - CMH'),
('CRP','Corpus Christi, TX - CRP'),
('DAL','Dallas (Love Field), TX - DAL'),
('DAY','Dayton, OH - DAY'),
('DEN','Denver, CO - DEN'),
('DSM','Des Moines, IA - DSM'),
('DTW','Detroit, MI - DTW'),
('ELP','El Paso, TX - ELP'),
('FNT','Flint, MI - FNT'),
('RSW','Ft. Myers, FL - RSW'),
('GRR','Grand Rapids, MI - GRR'),
('GSP','Greenville/Spartanburg, SC - GSP'),
('HRL','Harlingen, TX - HRL'),
('BDL','Hartford, CT - BDL'),
('HOU','Houston (Hobby), TX - HOU'),
('IND','Indianapolis, IN - IND'),
('JAX','Jacksonville, FL - JAX'),
('MCI','Kansas City, MO - MCI'),
('LAS','Las Vegas, NV - LAS'),
('LIR','Liberia, Costa Rica - LIR'),
('LIT','Little Rock, AR - LIT'),
('BUR','Burbank, CA - BUR'),
('LAX','Los Angeles, CA - LAX'),
('SDF','Louisville, KY - SDF'),
('LBB','Lubbock, TX - LBB'),
('MHT','Manchester, NH - MHT'),
('MEM','Memphis, TN - MEM'),
('MEX','Mexico City, Mexico - MEX'),
('FLL','Ft. Lauderdale, FL - FLL'),
('MAF','Midland/Odessa, TX - MAF'),
('MKE','Milwaukee, WI - MKE'),
('MSP','Minneapolis/St. Paul (Terminal 2), MN - MSP'),
('MBJ','Montego Bay, Jamaica - MBJ'),
('BNA','Nashville, TN - BNA'),
('NAS','Nassau, Bahamas - NAS'),
('MSY','New Orleans, LA - MSY'),
('ISP','Long Island/Islip, NY - ISP'),
('LGA','New York (LaGuardia), NY - LGA'),
('EWR','New York/Newark, NJ - EWR'),
('ORF','Norfolk, VA - ORF'),
('OKC','Oklahoma City, OK - OKC'),
('OMA','Omaha, NE - OMA'),
('ONT','Ontario/LA, CA - ONT'),
('SNA','Orange County/Santa Ana, CA - SNA'),
('MCO','Orlando, FL - MCO'),
('ECP','Panama City Beach, FL - ECP'),
('PNS','Pensacola, FL - PNS'),
('PHL','Philadelphia, PA - PHL'),
('PHX','Phoenix, AZ - PHX'),
('PIT','Pittsburgh, PA - PIT'),
('PDX','Portland, OR - PDX'),
('PWM','Portland, ME - PWM'),
('PVD','Providence, RI - PVD'),
('PVR','Puerto Vallarta, MX - PVR'),
('PUJ','Punta Cana, DR - PUJ'),
('RDU','Raleigh/Durham, NC - RDU'),
('RNO','Reno/Tahoe, NV - RNO'),
('RIC','Richmond, VA - RIC'),
('ROC','Rochester, NY - ROC'),
('SMF','Sacramento, CA - SMF'),
('SLC','Salt Lake City, UT - SLC'),
('SAT','San Antonio, TX - SAT'),
('SAN','San Diego, CA - SAN'),
('OAK','Oakland, CA - OAK'),
('SFO','San Francisco, CA - SFO'),
('SJC','San Jose, CA - SJC'),
('SJO','San Jose, Costa Rica - SJO'),
('SJU','San Juan, PR - SJU'),
('SEA','Seattle/Tacoma, WA - SEA'),
('GEG','Spokane, WA - GEG'),
('STL','St. Louis, MO - STL'),
('TPA','Tampa, FL - TPA'),
('TUS','Tucson, AZ - TUS'),
('TUL','Tulsa, OK - TUL'),
('BWI','Baltimore/Washington, MD - BWI'),
('IAD','Washington (Dulles), DC - IAD'),
('DCA','Washington (Reagan National), DC - DCA'),
('PBI','West Palm Beach, FL - PBI'),
('ICT','Wichita, KS - ICT');

/* ********************************** COMMIT ********************************** */

COMMIT WORK;

/* ****************************************************************************** */
