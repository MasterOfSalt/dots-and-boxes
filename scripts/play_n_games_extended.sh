#!/bin/bash
#------------------------------------------------------------------------------------------#
#       DE STANDAARD PLAY MET ENKEL 1STE TWEE PARAMS IS 10 GAMES OP EEN 4x4 BORD!
#------------------------------------------------------------------------------------------#
#p1,2           Agent player-types (v1,v2,v3,v4,v5,...)
#
#   don't forget to run your agent first!
#   e.g python3 dotsandboxesagent_v1_random_moves.py 2001
#
#from, till     Width(n) and height(m) of the puzzle which includes all its permutations of n and m 
#games          Amount of games to simulate
#parser         To automatically parse the simulated games
#learner        To automatic feed/learn this parsed data into our json tree data (only relevant to mcts)

# EXAMPLE:      bash play_n_games_extended.sh v1 v2 
#               bash play_n_games_extended.sh v1 v5 10 3 3  P L 

p1=$1
p2=$2
games=$3 
from=$4
till=$5
parser=$6       # set to 'P' to activate
learner=$7      # set to 'L' to activate

if [ $# -lt 2 ]
  then
    echo "Please supply at least the first 2 arguments! e.g.: bash play.sh v1 v2"
    exit 1
fi


if [ "$p1" == "v1" ]; then	ipaddr1="ws://127.0.0.1:2001"; fi
if [ "$p1" == "v2" ]; then	ipaddr1="ws://127.0.0.1:2002"; fi
if [ "$p1" == "v3" ]; then	ipaddr1="ws://127.0.0.1:2003"; fi
if [ "$p1" == "v3b" ]; then	ipaddr1="ws://127.0.0.1:20031"; fi
if [ "$p1" == "v4" ]; then	ipaddr1="ws://127.0.0.1:2004"; fi
if [ "$p1" == "v5" ]; then	ipaddr1="ws://127.0.0.1:2005"; fi
if [ "$p1" == "v6" ]; then	ipaddr1="ws://127.0.0.1:2006"; fi
if [ "$p2" == "v1" ]; then	ipaddr2="ws://127.0.0.1:2001"; fi
if [ "$p2" == "v2" ]; then	ipaddr2="ws://127.0.0.1:2002"; fi
if [ "$p2" == "v3" ]; then	ipaddr2="ws://127.0.0.1:2003"; fi
if [ "$p2" == "v3b" ]; then	ipaddr2="ws://127.0.0.1:20031"; fi
if [ "$p2" == "v4" ]; then	ipaddr2="ws://127.0.0.1:2004"; fi
if [ "$p2" == "v5" ]; then	ipaddr2="ws://127.0.0.1:2005"; fi
if [ "$p2" == "v6" ]; then	ipaddr2="ws://127.0.0.1:2006"; fi
if [ "$games" == "$NULL" ]; then	games=5; fi

if [ "$from" == "$NULL" ] || [ "$till" == "$NULL"]; then
    row=4
	col=4
    echo "Standard $games games started on a $from x $till board."
    for i in $(seq 1 $games);
    do
      echo "player1 is $p1 - $ipaddr1 & player2 is $p2 - $ipaddr2"
        python3 ../dotsandboxescompete.py $ipaddr1 $ipaddr2 -r $row -c $col 
      echo "finished game $i"
    done
else

    for row in $(seq 3 $from);
    do
      for col in $(seq 3 $till);
      do
        for i in $(seq 1 $games);
        do
          echo "started game $i for $row x $col "
          echo "player1 is $ipaddr1 & player2 is $ipaddr2"
            python3 ../dotsandboxescompete.py $ipaddr1 $ipaddr2 -r $row -c $col 
          echo "finished game $i"
        done
      done
    done

    for row in $(seq 3 $till);
    do
      for col in $(seq 3 $from);
      do
        for i in $(seq 1 $games);
        do
          echo "started game $i for $row x $col"
          python3 ../dotsandboxescompete.py $ipaddr1 $ipaddr2 -r $row -c $col
          echo "finished game $i"
        done
      done
    done
fi

if [ "$parser" == "P" ]; then
	echo "Started parsing..."
    python3 ../agents/parser.py
    echo "done parsing"
    if [ "$learner" == "L" ]; then
        echo "Started learning..."
        python3 ../agents/learner.py
        echo "done learning"
    else
        echo "data not learned"
    fi
else
    echo "Data not parsed"
fi



#bash script.sh 10 10 ws://localhost:2001 ws://localhost:2002
