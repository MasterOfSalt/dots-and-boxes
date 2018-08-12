#!/usr/bin/env python3
# encoding: utf-8
"""
dotsandboxescompete.py

Template for the Machine Learning Project course at KU Leuven (2017-2018)
of Hendrik Blockeel and Wannes Meert.

Copyright (c) 2018 KU Leuven. All rights reserved.
"""

import sys
import argparse
import logging
import asyncio
import websockets
import json
from collections import defaultdict
import random
import uuid
import time
import csv
import uuid
from timeit import Timer

logger = logging.getLogger(__name__)
import os
def transform_horizontal_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return abs(n-x),y,o
    if o == "v":
        return abs(n-x-1),y,o

def transform_vertical_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return x,abs(n-y-1),o
    if o == "v":
        return x,abs(n-y),o
def transform_90_nxn(coord,n):
    x,y,o = coord
    if o == "h":
        return y,abs(n-x),"v"
    if o == "v":
        return y,abs(n-x-1),"h"
#
def transform_180_nxn(coord,n):
    return transform_90_nxn(transform_90_nxn(coord,n),n)
def transform_270_nxn(coord,n):
    return transform_90_nxn(transform_180_nxn(coord,n),n)
def start_competition(address1, address2, nb_rows, nb_cols, timelimit):
   asyncio.get_event_loop().run_until_complete(connect_agent(address1, address2, nb_rows, nb_cols, timelimit))

async def connect_agent(uri1, uri2, nb_rows, nb_cols, timelimit):
    cur_game = str(uuid.uuid4())
    winner = None
    cells = []
    cur_player = 1
    points = [0, 0, 0]
    timings = [None, [], []]

    for ri in range(nb_rows + 1):
        columns = []
        for ci in range(nb_cols + 1):
            columns.append({"v":0, "h":0, "p":0})
        cells.append(columns)

    logger.info("Connecting to {}".format(uri1))
    async with websockets.connect(uri1) as websocket1:
        logger.info("Connecting to {}".format(uri2))
        async with websockets.connect(uri2) as websocket2:
            logger.info("Connected")

            # Start game
            msg = {
              "type": "start",
              "player": 1,
              "timelimit": timelimit,
              "game": cur_game,
              "grid": [nb_rows, nb_cols]
            }
            await websocket1.send(json.dumps(msg))
            msg["player"] = 2
            await websocket2.send(json.dumps(msg))
            moves = []

            player1 = "player1"
            player2 = "player2"
            if uri1 == "ws://localhost:2001" or uri1 == "ws://127.0.0.1:2001":
                p1 = "v1"
                player1 = "V1_RANDOM"
            if uri1 == "ws://localhost:2002" or uri1 == "ws://127.0.0.1:2002":
                p1 = "v2"
                player1 = "V2_ALPHABETA"
            if uri1 == "ws://localhost:2003" or uri1 == "ws://127.0.0.1:2003":
                p1 = "v3"
                player1 = "V3_HEURISTIC"
            if uri1 == "ws://localhost:20031" or uri1 == "ws://127.0.0.1:20031":
                p1 = "v3b"
                player1 = "V3_HEURISTICb"
            if uri1 == "ws://localhost:2005" or uri1 == "ws://127.0.0.1:2005":
                p1 = "v5"
                player1 = "V5_MCTS_always4never3"
            if uri2 == "ws://localhost:20051" or uri2 == "ws://127.0.0.1:20051":
                p2 = "v5"
                player2 = "V5_MCTS_minimax_score"
            if uri2 == "ws://localhost:20051" or uri2 == "ws://127.0.0.1:20051":
                p2 = "v5"
                player2 = "V5_MCTS_random"
            if uri2 == "ws://localhost:2001" or uri2 == "ws://127.0.0.1:2001":
                p2 = "v1"
                player2 = "V1_RANDOM"
            if uri2 == "ws://localhost:2002" or uri2 == "ws://127.0.0.1:2002":
                p2 = "v2"
                player2 = "V2_ALPHABETA"
            if uri2 == "ws://localhost:2003" or uri2 == "ws://127.0.0.1:2003":
                p2 = "v3"
                player2 = "V3_HEURISTIC"
            if uri2 == "ws://localhost:3003" or uri2 == "ws://127.0.0.1:3003":
                p2 = "v3"
                player2 = "V3_HEURISTIC"
            if uri2 == "ws://localhost:20031" or uri2 == "ws://127.0.0.1:20031":
                p2 = "v3b"
                player2 = "V3_HEURISTICb"
            if uri2 == "ws://localhost:2005" or uri2 == "ws://127.0.0.1:2005":
                p2 = "v5"
                player2 = "V5_MCTS_always4never3"
            if uri2 == "ws://localhost:20051" or uri2 == "ws://127.0.0.1:20051":
                p2 = "v5"
                player2 = "V5_MCTS_minimax_score"
            if uri2 == "ws://localhost:20052" or uri2 == "ws://127.0.0.1:20052":
                p2 = "v5"
                player2 = "V5_MCTS_random"

            # Run game
            while winner is None:
                ask_time = time.time()
                #logger.info("Waiting for player {}".format(cur_player))
                if cur_player == 1:
                    msg = await websocket1.recv()
                else:
                    msg = await websocket2.recv()
                recv_time = time.time()
                diff_time = recv_time - ask_time
                timings[cur_player].append(diff_time)
                #logger.info("Message received after (s): {}".format(diff_time))
                try:
                    msg = json.loads(msg)
                except json.decoder.JSONDecodeError as err:
                    logger.debug(err)
                    continue
                if msg["type"] != "action":
                    logger.error("Unknown message: {}".format(msg))
                    continue
                r, c = msg["location"]
                o = msg["orientation"]
                moves.append(str(r)+","+str(c)+","+str(o))
                next_player = user_action(r, c, o, cur_player,
                                          cells, points,
                                          nb_rows, nb_cols)


                if points[1] + points[2] == nb_cols * nb_rows:
                    # Game over
                    winner = 1
                    id = uuid.uuid1()


                    if points[2] == points[1]:
                        winner = 0
                    if points[2] > points[1]:
                        winner = 2

                    folder = str(nb_rows) + "x" + str(nb_cols)
                    name = "game-"+str(nb_rows)+"-"+str(nb_cols)+"-"+str(id)+"-"+str(p1)+"-"+str(p2)+"_"+str(winner)+".json"
                    '''
                            if not os.path.exists("data/"+folder):
                            if uri1 == "ws://127.0.0.1:2005" or uri2 == "ws://127.0.0.1:2005":
                                os.makedirs("../data/version5/"+folder+"/unprocessed/", exist_ok=True)
                                jfile = open("../data/version5/"+folder+"/unprocessed/"+name,'w+')
                                json.dump(moves,jfile)
                            else:
                    '''
                    os.makedirs("../data/"+folder, exist_ok=True)
                    jfile = open("../data/"+folder+"/unprocessed/"+name,'w+')
                    json.dump(moves,jfile)
                    movesh = []
                    movesv = []
                    nxn = (nb_rows == nb_cols)
                    moves90 = []
                    moves180 = []
                    moves270 = []
                    for move in moves:
                        realmove = move.split(',')
                        movesv.append(transform_vertical_nxn((int(realmove[0]),int(realmove[1]),str(realmove[2])),nb_cols))
                        movesh.append(transform_horizontal_nxn((int(realmove[0]),int(realmove[1]),str(realmove[2])),nb_rows))
                        if nxn:
                            moves90.append(transform_90_nxn((int(realmove[0]),int(realmove[1]),str(realmove[2])),nb_rows))
                            moves180.append(transform_180_nxn((int(realmove[0]),int(realmove[1]),str(realmove[2])),nb_rows))
                            moves270.append(transform_270_nxn((int(realmove[0]),int(realmove[1]),str(realmove[2])),nb_rows))
                    jfile2 = open("../data/"+folder+"/unprocessed/"+"v"+name,'w+')
                    json.dump(movesv,jfile2)
                    jfile3 = open("../data/"+folder+"/unprocessed/"+"h"+name,'w+')
                    json.dump(movesh,jfile3)
                    if nxn:
                        jfile4 = open("../data/"+folder+"/unprocessed/"+"90"+name,'w+')
                        json.dump(moves90,jfile4)
                        jfile5 = open("../data/"+folder+"/unprocessed/"+"180"+name,'w+')
                        json.dump(moves180,jfile5)
                        jfile6 = open("../data/"+folder+"/unprocessed/"+"270"+name,'w+')
                        json.dump(moves270,jfile6)

                else:
                    msg = {
                        "type": "action",
                        "game": cur_game,
                        "player": cur_player,
                        "nextplayer": next_player,
                        "score": [points[1], points[2]],
                        "location": [r, c],
                        "orientation": o
                    }
                    await websocket1.send(json.dumps(msg))
                    await websocket2.send(json.dumps(msg))

                cur_player = next_player

            # End game
            logger.info("Game ended: points1={} - points2={} - winner={}".format(points[1], points[2], winner))
            msg = {
                "type": "end",
                "game": cur_game,
                "player": cur_player,
                "nextplayer": 0,
                "score": [points[1], points[2]],
                "location": [r, c],
                "orientation": o,
                "winner": winner
            }
            f = open('../data/data.csv', 'a')
            writer = csv.writer(f)

            if winner == 1:
                winnerstring = player1
            else:
                winnerstring = player2
            dimension = str(nb_rows)+"x"+str(nb_cols)
            row = [player1,player2,winnerstring,dimension]
            writer.writerow(row)
            await websocket1.send(json.dumps(msg))
            await websocket2.send(json.dumps(msg))

    # Timings
    # for i in [1, 2]:
    #     logger.info("Timings: player={} - avg={} - min={} - max={}"\
    #         .format(i,
    #                 sum(timings[i])/len(timings[i]),
    #                 min(timings[i]),
    #                 max(timings[i])))

    logger.info("Closed connections")


def user_action(r, c, o, cur_player, cells, points, nb_rows, nb_cols):
    #logger.info("User action: player={} - r={} - c={} - o={}".format(cur_player, r, c, o))
    next_player = cur_player
    won_cell = False
    cell = cells[int(r)][int(c)]
    if o == "h":
        if cell["h"] != 0:
            return cur_player
        cell["h"] = cur_player
        # Above
        if int(r) > 0:
            if cells[r - 1][c]["v"] != 0 \
                and cells[r - 1][c + 1]["v"] != 0 \
                and cells[r - 1][c]["h"] != 0 \
                and cells[r][c]["h"] != 0:
                won_cell = True
                points[cur_player] += 1
                cells[r - 1][c]["p"] = cur_player
        # Below
        if int(r) < nb_rows:
            if cells[r][c]["v"] != 0 \
                and cells[r][c + 1]["v"] != 0 \
                and cells[r][c]["h"] != 0 \
                and cells[r + 1][c]["h"] != 0:
                won_cell = True
                points[cur_player] += 1
                cells[r][c]["p"] = cur_player

    if o == "v":
        if cell["v"] != 0:
            return cur_player
        cell["v"] = cur_player;
        # Left
        if int(c) > 0:
            if cells[int(r)][int(c) - 1]["v"] != 0 \
                and cells[r][c]["v"] != 0 \
                and cells[r][c - 1]["h"] != 0 \
                and cells[r + 1][c - 1]["h"] != 0:
                won_cell = True
                points[cur_player] += 1
                cells[r][c - 1]["p"] = cur_player
        # Right
        if int(c) < nb_cols:
            if cells[int(r)][int(c)]["v"] != 0 \
                and cells[int(r)][int(c) + 1]["v"] != 0 \
                and cells[int(r)][int(c)]["h"] != 0 \
                and cells[int(r) + 1][int(c)]["h"] != 0:
                won_cell = True
                points[cur_player] += 1
                cells[r][c]["p"] = cur_player

    if not won_cell:
        next_player = 3 - cur_player
    else:
        next_player = cur_player
        #print("Update points: player1={} - player2={}".format(points[1], points[2]))
    return next_player


def main(argv=None):
    parser = argparse.ArgumentParser(description='Start agent to play Dots and Boxes')
    parser.add_argument('--verbose', '-v', action='count', default=0, help='Verbose output')
    parser.add_argument('--quiet', '-q', action='count', default=0, help='Quiet output')
    parser.add_argument('--cols', '-c', type=int, default=2, help='Number of columns')
    parser.add_argument('--rows', '-r', type=int, default=2, help='Number of rows')
    parser.add_argument('--timelimit', '-t', type=float, default=0.5, help='Time limit per request in seconds')
    parser.add_argument('agents', nargs=2, metavar='AGENT', help='Websockets addresses for agents')
    args = parser.parse_args(argv)

    logger.setLevel(max(logging.INFO - 10 * (args.verbose - args.quiet), logging.DEBUG))
    logger.addHandler(logging.StreamHandler(sys.stdout))

    start_competition(args.agents[0], args.agents[1], args.rows, args.cols, args.timelimit)


if __name__ == "__main__":
    sys.exit(main())
