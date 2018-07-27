Dots and Boxes application
==========================

![Screenshot of Dots and Boxes](https://people.cs.kuleuven.be/wannes.meert/dotsandboxes/screenshot.png?v=2)

This setup is part of the course "Machine Learning: Project" (KU Leuven,
Faculty of engineering, Department of Computer Science,
[DTAI research group](https://dtai.cs.kuleuven.be)).


Installation
------------

The example agent is designed for Python 3.6. Dependencies can be
installed using pip:

    $ pip install -r requirements.txt


Start the game GUI
------------------
This program shows a web-based GUI to play the Dots and Boxes
game. This supports human-human, agent-human and agent-agent combinations.
It is a simple Javascript based application that runs entirely in the browser.
You can start it by opening the file `static/dotsandboxes.html` in a browser.
Or alternatively, you can start the app using the included simple server:

    $ ./dotsandboxesserver.py 8001

The game can then be played by directing your browser to http://127.0.0.1:8001.

Flow
------------------
The `dotsandboxescompete.py` file creates a .json game file which contains the winner in it's filename
The `learner.py` processes all the .json files of a specific board type andcreate a .json file of the tree data. 
The `parser.py` uses this game-XX-XX.json file to create yet another .json file which serves our GUI.

Run the Parser: e.g. `parser.py`. This creates/appends a json file for the gui. (score.html)   
Run the Leaner: e.g. `parser.py 3 4`. This learns all unprocessed 3x4 games.   


Run simulations of the game
------------------
The directory `scripts/*.sh` contains scripts that you can use to quickly run alot of games
and immediatly parse/learn them.

E.g

    $ bash play_n_games.sh v1 v2 10 4 4 P L 
    
* **$1** — Player 1 (this can be "v1","v2","v3",...)
* **$2** — Player 1 (this can be "v1","v2","v3",...)
* **$3** — Number of games
* **$4** — Rows 
* **$5** — Columns 
* **$6** — Parse the data afterwards
* **$7** — Learn the data afterwards

E.g

    $ bash play_nxm_games_extended.sh v1 v2 20 5 5  P L 
    
* **$4** — Rows (actually permutations up to this column).
* **$5** — Columns (actually permutations up to this column).
* **$6** — Parse the data afterwards
* **$7** — Learn the data afterwards

Start the agent client
----------------------

Starting the agent client is done using the following command:

    $ ./dotsandboxesagent <port>

This starts a websocket on the given port that can receveive JSON messages.

The JSON messages given below should be handled by your agent.
Take into account the maximal time allowed to reply.

### Initiate the game

Both players get a message that a new game has started:

    {
        "type": "start",
        "player": 1,
        "timelimit", 0.5,
        "grid": [5, 5],
        "game": "123456"
    }

where `player` is the number assigned to this agent, `timelimit` is the
time in seconds in which you need to send your action back to the server,
and `grid` is the grid size in rows and columns.

If you are player 1, reply with the first action you want to perform:

    {
        "type": "action",
        "location": [1, 1],
        "orientation": "v"
    }

The field `location` is expressed as row and column (zero-based numbering) and
`orientation` is either "v" (vertical) or "h" (horizontal).


### Action in the game

When an action is played, the message sent to both players is:

    {
        "type": "action",
        "game": "123456",
        "player": 1,
        "nextplayer": 2,
        "score": [0, 0],
        "location": [1, 1],
        "orientation": "v"
    }


If it is your turn you should answer with a message that states your next
move:

    {
        "type": "action",
        "location": [1, 1],
        "orientation": "v"
    }


### Game end

When the game ends after an action, the message is slightly altered:

    {
        "type": "end",
        "game": "123456",
        "player": 1,
        "nextplayer": 0,
        "score": [3, 1],
        "location": [1, 1],
        "orientation": "v",
        "winner": 1
    }

The `type` field becomes `end` and a new field `winner` is set to the player
that has won the game.


