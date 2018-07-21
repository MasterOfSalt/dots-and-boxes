#!/bin/bash
#
# EXAMPLE:      bash play_n_games.sh 10 v1 v2 4 4
# 
N=$1
p1=$2
p2=$3
C=$4
R=$5

if [ "$p1" == "v1" ]; then	ipaddr1="ws://127.0.0.1:2001"; fi
if [ "$p1" == "v2" ]; then	ipaddr1="ws://127.0.0.1:2002"; fi
if [ "$p1" == "v3" ]; then	ipaddr1="ws://127.0.0.1:2003"; fi
if [ "$p1" == "v4" ]; then	ipaddr1="ws://127.0.0.1:2004"; fi
if [ "$p1" == "v5" ]; then	ipaddr1="ws://127.0.0.1:2005"; fi
if [ "$p1" == "v6" ]; then	ipaddr1="ws://127.0.0.1:2006"; fi
if [ "$p2" == "v1" ]; then	ipaddr2="ws://127.0.0.1:2001"; fi
if [ "$p2" == "v2" ]; then	ipaddr2="ws://127.0.0.1:2002"; fi
if [ "$p2" == "v3" ]; then	ipaddr2="ws://127.0.0.1:2003"; fi
if [ "$p2" == "v4" ]; then	ipaddr2="ws://127.0.0.1:2004"; fi
if [ "$p2" == "v5" ]; then	ipaddr2="ws://127.0.0.1:2005"; fi
if [ "$p2" == "v6" ]; then	ipaddr2="ws://127.0.0.1:2006"; fi

for row in $(seq 1 $N);
do
  python3 ../dotsandboxescompete.py $ipaddr1 $ipaddr2 -r $R -c $C 
done
