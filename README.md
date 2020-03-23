# SQL SCRIPT TO CREATE AND ADD TO THE TABLE PRESIDENTS


CREATE TABLE mstallter_Presidents(
	NUM int not null,
	FIRSTNAME varchar(255),
	LASTNAME varchar(255),
	AGE int,
	HOMESTATE varchar(255),
	HOMECITY varchar(255),
	TERMS int,
    YROFFRSTTERM int,
	primary key (NUM)
);

INSERT INTO mstallter_Presidents
VALUES(45, "Donald", "Trump", 73, "New York", "New York", 1, 2016),
(44, "Barack", "Obama", 58, "Hawaii", "Honolulu", 2, 2008),
(43, "George", "Bush", 73, "Connecticut", "New Haven", 2, 2000),
(42, "Bill", "Clinton", 73, "Arkansas", "Hope", 2, 1992),
(41, "George HW", "Bush", 94, "California", "Los Angeles", 1, 1988),
(40, "Ronald", "Reagan", 93, "Illinois", "Tampico", 2, 1980),
(39, "Jimmy", "Carter", 95, "Georgia", "Plains", 1, 1976);

