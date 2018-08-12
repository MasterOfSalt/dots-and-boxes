#!/bin/bash
#
# EXAMPLE:      bash play_n_games.sh v1 v2 10 4 4 P L
#

p1=$1
p2=$2
N=$3
R=$4
C=$5

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
if [ "$p2" == "v3" ]; then	ipaddr2="ws://127.0.0.1:3003"; fi
if [ "$p2" == "v3b" ]; then	ipaddr2="ws://127.0.0.1:20031"; fi
if [ "$p2" == "v4" ]; then	ipaddr2="ws://127.0.0.1:2004"; fi
if [ "$p2" == "v5" ]; then	ipaddr2="ws://127.0.0.1:2005"; fi
if [ "$p2" == "v6" ]; then	ipaddr2="ws://127.0.0.1:2006"; fi

for row in $(seq 1 $N);
do
  python3 ../dotsandboxescompete.py $ipaddr1 $ipaddr2 -r $R -c $C
done


parser=$6       # set to 'P' to activate
learner=$7      # set to 'L' to activate
if [ "$parser" == "P" ]; then
	echo "Started parsing..."
    python3 ../agents/parser.py
    echo "done parsing"
    if [ "$learner" == "L" ]; then
        echo "Started learning..."
        python3 ../agents/learner.py $R $C
        echo "done learning"
    else
        echo "data not learned"
    fi
else
    echo "Data not parsed"
fi
