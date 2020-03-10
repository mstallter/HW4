# SQL SCRIPT TO CREATE AND ADD TO THE TABLE PRESIDENTS


CREATE TABLE Presidents(
	FIRSTNAME varchar(255),
	LASTNAME varchar(255),
	AGE int,
	STATE varchar(255),
	CITY varchar(255),
	TERMS int,
    YROFFRSTTERM int
);

INSERT INTO Presidents
VALUES("Donald", "Trump", 73, "New York", "New York", 1, 2016),
("Barack", "Obama", 58, "Hawaii", "Honolulu", 2, 2008),
("George", "Bush", 73, "Connecticut", "New Haven", 2, 2000),
("Bill", "Clinton", 73, "Arkansas", "Hope", 2, 1992),
("George HW", "Bush", 94, "California", "Los Angeles", 1, 1988),
("Ronald", "Reagan", 93, "Illinois", "Tampico", 2, 1980),
("Jimmy", "Carter", 95, "Georgia", "Plains", 1, 1976);

