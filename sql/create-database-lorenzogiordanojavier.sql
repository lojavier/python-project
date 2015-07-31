START TRANSACTION;

/* ******************************** CREATE DATABASE ******************************** */

CREATE DATABASE IF NOT EXISTS lorenzogiordanojavierdb
CHARACTER SET utf8 COLLATE utf8_general_ci;

/* ****************************************************************************** */
/* ******************************** CREATE TABLE ******************************** */

CREATE TABLE IF NOT EXISTS lorenzogiordanojavierdb.personal_info (
FIRST_NAME				VARCHAR(255) NOT NULL,
MIDDLE_NAME				VARCHAR(255) NOT NULL,
LAST_NAME				VARCHAR(255) NOT NULL,
ADDRESS_1				VARCHAR(255) NOT NULL,
ADDRESS_2				VARCHAR(255) DEFAULT NULL,
CITY					VARCHAR(255) NOT NULL,
STATE					VARCHAR(255) NOT NULL,
ZIP_CODE				INT(5) NOT NULL,
COUNTRY					VARCHAR(255) NOT NULL,
HOME_PHONE				VARCHAR(10) DEFAULT NULL,
CELL_PHONE				VARCHAR(10) NOT NULL,
EMAIL					VARCHAR(255) NOT NULL,
BIRTH_DATE				TIMESTAMP NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='personal info';

CREATE TABLE IF NOT EXISTS lorenzogiordanojavierdb.employment_history (
COMPANY_NAME			VARCHAR(255) NOT NULL,
STREET_ADDRESS_1		VARCHAR(255) NOT NULL,
STREET_ADDRESS_2		VARCHAR(255) DEFAULT NULL,
CITY					VARCHAR(255) NOT NULL,
STATE					VARCHAR(255) NOT NULL,
ZIP_CODE				INT(5) NOT NULL,
COUNTRY					VARCHAR(255) NOT NULL,
WORK_PHONE				VARCHAR(10) DEFAULT NULL,
POSITION_TITLE			VARCHAR(255) DEFAULT NULL,
DESCRIPTION_1			TEXT,
DESCRIPTION_2			TEXT,
DESCRIPTION_3			TEXT,
DESCRIPTION_4			TEXT,
DESCRIPTION_5			TEXT,
START_DATE				TIMESTAMP NOT NULL,
END_DATE				TIMESTAMP NULL DEFAULT NULL,
PRESENTLY_EMPLOYED_FLAG	TINYINT(1) NOT NULL DEFAULT '0',
COMPANY_LOGO			VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='employment history';

CREATE TABLE IF NOT EXISTS lorenzogiordanojavierdb.education (
SCHOOL_NAME				VARCHAR(255) NOT NULL,
ADDRESS_1				VARCHAR(255) NOT NULL,
ADDRESS_2				VARCHAR(255) DEFAULT NULL,
CITY					VARCHAR(255) NOT NULL,
STATE					VARCHAR(255) NOT NULL,
ZIP_CODE				INT(5) NOT NULL,
COUNTRY					VARCHAR(255) NOT NULL,
WORK_PHONE				VARCHAR(10) NOT NULL,
SCHOOL_URL				VARCHAR(255) NOT NULL,
SCHOOL_LOGO				VARCHAR(255) NOT NULL,
SCHOOL_CATEGORY			VARCHAR(255) NOT NULL,
DEGREE_TYPE				VARCHAR(255) NOT NULL,
MAJOR					VARCHAR(255) DEFAULT NULL,
MINOR					VARCHAR(255) DEFAULT NULL,
GPA						DOUBLE(2,1) DEFAULT NULL,
START_DATE				TIMESTAMP NOT NULL,
END_DATE				TIMESTAMP NULL DEFAULT NULL,
PRESENTLY_ATTENDING_FLAG TINYINT(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='education';

/* ***************************************************************************** */
/* ******************************** INSERT INTO ******************************** */

INSERT INTO lorenzogiordanojavierdb.education (SCHOOL_NAME,ADDRESS_1,ADDRESS_2,CITY,STATE,ZIP_CODE,COUNTRY,WORK_PHONE,SCHOOL_URL,SCHOOL_LOGO,DEGREE_TYPE,SCHOOL_CATEGORY,MAJOR,MINOR,GPA,START_DATE,END_DATE,PRESENTLY_ATTENDING_FLAG) VALUES
('San Jose State University','1 Washington Square',NULL,'San Jose','California',95192,'United States','4089241000','http://www.sjsu.edu','img/sjsulogo.png','Public University','Bachelor of Science','Computer Engineering','Mathematics',3.2,'2008-08-24 00:00:00','2014-12-18 00:00:00',0),
('California High School','9870 Broadmoor Drive',NULL,'San Ramon','California',94583,'United States','9258033200','http://www.calhigh.net','img/chslogo.png','Public High School','High School Diploma',NULL,NULL,3.3,'2004-08-24 00:00:00','2008-06-15 00:00:00',0);

INSERT INTO lorenzogiordanojavierdb.personal_info (FIRST_NAME,MIDDLE_NAME,LAST_NAME,ADDRESS_1,ADDRESS_2,CITY,STATE,ZIP_CODE,COUNTRY,HOME_PHONE,CELL_PHONE,EMAIL,BIRTH_DATE) VALUES
('Lorenzo','Giordano','Javier','68 Fife Court',NULL,'San Ramon','California',94583,'United States','9255510465','9252007284','loj90@sbcglobal.net','1990-02-06 19:01:00');


/* ********************************** COMMIT ********************************** */

COMMIT WORK;

/* ****************************************************************************** */