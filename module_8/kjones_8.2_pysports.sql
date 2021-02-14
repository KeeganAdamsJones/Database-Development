
-- Title: Module 8.2 PySports Database
-- Author: Keegan Jones
-- Date: 2/8/2021
-- Description: MySQL database for PySports

--Drop test user if exists. 
DROP USER IF EXISTS 'pysports_user'@'localhost';

-- Create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

-- Create team table.
CREATE TABLE team (
    team_id     INT             NOT NULL      AUTO_INCREMENT,
    team_name   CHAR(20)        NOT NULL,
    mascot      CHAR(20)        NOT NULL,
    PRIMARY KEY(team_id)
);

-- Create player table.
CREATE TABLE player (
    player_id       INT         NOT NULL       AUTO_INCREMENT,
    first_name      CHAR(20)    NOT NULL,
    last_name       CHAR(20)    NOT NULL,
    team_id			INT         NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id) 
        REFERENCES team(team_id)
);
-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Kids', 'Wild Animals');

INSERT INTO team(team_name, mascot)
    VALUES('Team Parents', 'Animal Trainers');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Nellie', 'Jones', (SELECT team_id FROM team WHERE team_name = 'Team Kids'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Olivia', 'Jones', (SELECT team_id FROM team WHERE team_name = 'Team Kids'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Afton', 'Jones', (SELECT team_id FROM team WHERE team_name = 'Team Kids'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Keegan', 'Jones', (SELECT team_id FROM team WHERE team_name = 'Team Parents'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jody', 'Jones', (SELECT team_id FROM team WHERE team_name = 'Team Parents'));


