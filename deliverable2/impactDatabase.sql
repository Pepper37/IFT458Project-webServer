CREATE DATABASE impact;
use impact;

CREATE TABLE events(
    eventID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    eventName VARCHAR(50) NOT NULL,
    eventDescription VARCHAR(300),
    street VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state char(2) NOT NULL,
    zip INT UNSIGNED NOT NULL,
    phone VARCHAR(12) NOT NULL,
    eventDate DATE NOT NULL
);

CREATE TABLE offices(
    officeID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    officeName VARCHAR(50) NOT NULL,
    officeDescription VARCHAR(300),
    street VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state char(2) NOT NULL,
    zip INT UNSIGNED NOT NULL,
    phone VARCHAR(12) NOT NULL,
    budget FLOAT NOT NULL 
);

CREATE TABLE volunteers(
    username VARCHAR(8) NOT NULL PRIMARY KEY,
    vollunteerPassword VARCHAR(8) NOT NULL,
    firstName VARCHAR(40) NOT NULL,
    middleName VARCHAR(40),
    lastName VARCHAR(40) NOT NULL,
    email VARCHAR(50) NOT NULL,
    street VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state char(2) NOT NULL,
    zip INT UNSIGNED NOT NULL,
    phone VARCHAR(12) NOT NULL,
    country VARCHAR(20) NOT NULL,
    gender enum('M', 'F', 'NB', 'Prefer Not To Say', 'Other') NOT NULL,
    dob DATE NOT NULL,
    memberOrg VARCHAR(100),
    
    leaderID VARCHAR(8) NOT NULL,
    CONSTRAINT volunteerFK
    FOREIGN KEY(leaderID)
    REFERENCES volunteers(username)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE officers(
    officerID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    officerRespons VARCHAR(300) NOT NULL,
    jobTitle VARCHAR(20) NOT NULL,
    dob DATE NOT NULL,
    firstName VARCHAR(40) NOT NULL,
    middleName VARCHAR(40),
    lastName VARCHAR(40) NOT NULL,
    password VARCHAR(20) NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE,
    
    officeID INT UNSIGNED NOT NULL,
    CONSTRAINT officerOfficeFK
    FOREIGN KEY(officeID)
    REFERENCES offices(officeID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    eventID INT UNSIGNED NOT NULL,
    CONSTRAINT officerEventFK
    FOREIGN KEY(eventID)
    REFERENCES events(eventID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE registers_for(
    volunteerID VARCHAR(8) NOT NULL,
    CONSTRAINT volunteerRegistersForFK
    FOREIGN KEY(volunteerID)
    REFERENCES volunteers(username)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    eventID INT UNSIGNED NOT NULL,
    CONSTRAINT registersForEventFK
    FOREIGN KEY(eventID)
    REFERENCES events(eventID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    PRIMARY KEY(volunteerID, eventID)
);
