-- Table definitions for the tournament project.

--Create tournament database
CREATE DATABASE tournament;

--Connects to the tournament database
\c tournament

--Creates players table
CREATE TABLE players ( id SERIAL PRIMARY KEY,
                        name TEXT);

--Creates matches table
CREATE TABLE matches ( id SERIAL PRIMARY KEY,
                        winner INTEGER REFERENCES players (id),
                        loser INTEGER REFERENCES players (id));

-- Displays each players win totals and total matches
CREATE VIEW standings AS
    SELECT players.id, players.name,
    (SELECT count(matches.winner) FROM matches WHERE players.id = matches.winner) AS Wins,
    (SELECT count(matches.id) FROM matches WHERE players.id = matches.winner OR players.id = matches.loser) AS Matches
    FROM players
    ORDER BY Wins DESC;

