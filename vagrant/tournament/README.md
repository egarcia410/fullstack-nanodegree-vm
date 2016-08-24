# Tournament Results
###### Udacity's Full Stack Web Developer Nanodegree
----


Develop a database schema to store the game matches between players and then write code to query this data and determine the winners of various games.


## Files
| File | Description |
|------|-------------|
| **tournament.py**  | This file is used to provide access to your database via a library of functions which can add, delete or query data in your database to another python program (a client program).  |
| **tournament.sql** | This file is used to set up your database schema (the table representation of your data structure). |
| **tournament_test.py** | This is a client program which will use your functions written in the tournament.py module. We've written this client program to test your implementation of functions in tournament.py |



## Installation And Usage:
#### Prerequisites:

| Program | Download |
|---------------|----------|
| **Virtual Box** | [download](https://www.virtualbox.org/wiki/Downloads)|
| **Vagrant** |  [download](https://www.vagrantup.com/downloads)       |

1. Open terminal
    - Run: `$ git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack`
    - This will create a new directory titled *fullstack* that contains all of the necessary configurations to run this application.
2. Move to the *vagrant* folder by entering:
    - `$ cd fullstack/vagrant/`
3. Using Git, clone this project:
    - Run: `$ git clone https://github.com/egarcia410/tournament tournament`
    - This will create a directory inside the *vagrant* directory titled *tournament*.
4. Run Vagrant by entering:
    - Run: ` $ vagrant up`
    - In less than a minute, this command will finish and you will have a virtual machine running Ubuntu.
5. SSH into the machine:
    - Run: `$ vagrant ssh`
    - This command will drop you into a full-fledged SSH session.
6. Move to the *tournament* folder  by entering:
    - Run: `$ cd /vagrant/tournament`
7. Launch psql command line interface
    - Run: `$ psql`
8. Initialize database and connects
    - Run: `\i tournament.sql`
    - This executes the sql commands within the sql file from psql
9. Open a second tab in the terminal
10. Repeat Steps #5 & #6
11. Run tournment test file
    - Run: `$ python tournament_test.sql`
    - See desired results below

```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```

## Functions
| tournament.py functions | Action |
|---------------|----------|
| **connect**  | Meant to connect to the database. |
| **deleteMatches**  |  Remove all the matches records from the database.      |
| **deletePlayers**  |  Remove all the player records from the database.      |
| **countPlayers**  |  Returns the number of players currently registered.      |
| **registerPlayer**  |  Adds a player to the tournament database.      |
| **playerStandings**  |  Returns a list of the players and their win records, sorted by wins.      |
| **reportMatch**  |  This is to simply populate the matches table and record the winner and loser as (winner,loser) in the insert statement.    |
| **swissPairings**  |  Returns a list of pairs of players for the next round of a match.      |


## License
Licensed under the MIT License (MIT)

```
Copyright (c) [2016] [Emmanuel Garcia]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```



