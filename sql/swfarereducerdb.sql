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
LAST_NAME					VARCHAR(255) NOT NULL,
EMAIL						VARCHAR(255) NOT NULL,
ORIGIN_AIRPORT_CODE     	VARCHAR(3) DEFAULT NULL,
DESTINATION_AIRPORT_CODE	VARCHAR(3) DEFAULT NULL,
DEPART_DATE					VARCHAR(10) DEFAULT NULL,
DEPART_TIME					VARCHAR(7) DEFAULT NULL,
ARRIVE_TIME					VARCHAR(7) DEFAULT NULL,
FLIGHT_NUM					VARCHAR(9) DEFAULT NULL,
PAID_DOLLARS				VARCHAR(6) NOT NULL DEFAULT '0',
PAID_POINTS					VARCHAR(6) NOT NULL DEFAULT '0',
FARE_TYPE					VARCHAR(15) NOT NULL DEFAULT 'Wanna Get Away',
LAST_ALERT					TIMESTAMP NULL,
SUBMISSION_DATE				TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (UPCOMING_FLIGHT_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='UPCOMING FLIGHTS' AUTO_INCREMENT=100000;

CREATE TABLE IF NOT EXISTS SWFAREREDUCERDB.WIRELESS_CARRIERS (
WIRELESS_CARRIER_ID			INT(11) NOT NULL AUTO_INCREMENT,
CARRIER_NAME				VARCHAR(255) NOT NULL,
CARRIER_TEXT_EMAIL			VARCHAR(255) NOT NULL,
PRIMARY KEY (WIRELESS_CARRIER_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='WIRELESS CARRIERS' AUTO_INCREMENT=1;

/* ***************************************************************************** */
/* ******************************** INSERT INTO ******************************** */

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
('Verizon','@vtext.com'),
('Virgin Mobile','@vmobl.com');

INSERT INTO SWFAREREDUCERDB.UPCOMING_FLIGHTS (CONFIRMATION_NUM,FIRST_NAME,LAST_NAME,EMAIL,ORIGIN_AIRPORT_CODE,DESTINATION_AIRPORT_CODE,DEPART_DATE,DEPART_TIME,ARRIVE_TIME,FLIGHT_NUM,PAID_DOLLARS,PAID_POINTS,FARE_TYPE) VALUES 
('8ABYGC','Lorenzo','Javier','9252007284@vtext.com','SJC','PHX','10/02/2015','8:05PM','9:50PM','179','0','4291','Wanna Get Away'),
('8ABYGC','Lorenzo','Javier','9252007284@vtext.com','PHX','SJC','10/06/2015','5:40AM','7:35AM','2787','0','2989','Wanna Get Away'),
('HHGRHL','Lorenzo','Javier','9252007284@vtext.com','SJC','ONT','10/30/2015','8:20PM','9:30PM','2953','0','6798','Wanna Get Away'),
('HN9RRZ','Lorenzo','Javier','9252007284@vtext.com','LAX','SJC','11/02/2015','8:45AM','9:55AM','1147','0','2924','Wanna Get Away'),
('832STR','Lorenzo','Javier','9252007284@vtext.com','SJC','PHX','11/04/2015','6:35AM','9:20AM','539','0','2989','Wanna Get Away'),
('832STR','Lorenzo','Javier','9252007284@vtext.com','PHX','SJC','11/08/2015','8:40PM','9:35PM','1117','0','8459','Wanna Get Away'),
('8J9T7V','Danielle','Gonzalez','9095698490@txt.att.net','ONT','SJC','09/03/2015','6:10AM','7:20AM','2964','56','0','Wanna Get Away'),
('8J9T7V','Danielle','Gonzalez','9095698490@txt.att.net','SJC','ONT','09/09/2015','8:20PM','9:30PM','2953','58','0','Wanna Get Away'),
('H9CRR8','Giovanni','Javier','9257856233@vtext.com','OAK','ONT','10/30/2015','8:40AM','9:55AM','2751','0','3542','Wanna Get Away'),
('H38RR6','Giovanni','Javier','9257856233@vtext.com','LAX','OAK','11/02/2015','9:15AM','10:30AM','2906','0','2924','Wanna Get Away');
-- INSERT INTO SWFAREREDUCERDB.UPCOMING_FLIGHTS (CONFIRMATION_NUM,FIRST_NAME,LAST_NAME,EMAIL,ORIGIN_AIRPORT_CODE,DESTINATION_AIRPORT_CODE,DEPART_DATE,DEPART_TIME,ARRIVE_DATE,FLIGHT_NUM,PAID_DOLLARS,PAID_POINTS) VALUES ();

/* ********************************** COMMIT ********************************** */

COMMIT WORK;

/* ****************************************************************************** */