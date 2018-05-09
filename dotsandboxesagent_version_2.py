#!/usr/bin/env python3
# encoding: utf-8
from version2.coins_strings_board import Coins_strings_board
import version2.alpha_beta_v1 as abv1
"""
dotsandboxesagent.py

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


logger = logging.getLogger(__name__)
games = {}
agentclass = None


class DotsAndBoxesAgent:
    """
    A DotsAndBoxesAgent object should implement the following methods:
    - __init__
    - add_player
    - register_action
    - next_action
    - end_game

    This class does not necessarily use the best data structures for the
    approach you want to use.
    """
    def __init__(self, player, nb_rows, nb_cols, timelimit):
        """Create Dots and Boxes agent.

        :param player: Player number, 1 or 2
        :param nb_rows: Rows in grid
        :param nb_cols: Columns in grid
        :param timelimit: Maximum time allowed to send a next action.
        """
        self.player = {player}
        self.timelimit = timelimit
        self.ended = False
        self.board = Coins_strings_board(nb_rows+1,nb_cols+1)
        self.odds = []
        self.evens = []
        i = 0
        while i<120:
            if(i%2==0):
                self.evens.append(i)
            else:
                self.odds.append(i)
            i += 1


    def add_player(self, player):
        """Use the same agent for multiple players."""
        self.player.add(player)

    def register_action(self, y, x, orientation, player):
        """
        INPUT
        Register action played in game after conversion to string board
        :param row:
        :param columns:
        :param orientation: "v" or "h"
        :param player: 1 or 2
        """
        """
        OUTPUT
        :param: number
        :param: number
        """
        if (orientation == "h"):
            a = self.evens[y]
            b = self.odds[x]
        else:
            a = self.odds[y]
            b = self.evens[x]
        self.board.fill_line(a,b,player)

    def next_action(self):
        """Return the next action this agent wants to perform.
        :return: (row, col, orientation)
        :return: (y, x, orientation)
        """
        # logger.info("Computing next move (grid={}x{}, player={})"\
        #         .format(self.board.nb_rows, self.board.nb_cols, self.player))

        free_lines = self.board.free_lines()
        print (free_lines)
        if len(free_lines) == 0:
            # Board full
            return None
        (a,b,score) = abv1.alphabeta(self.board,depth = 3,player = list(self.player)[0])
        if a%2==0:
            x = self.odds.index(b)
            y = self.evens.index(a)
            print("robot played H:",x,y)
            return (y,x,"h")
        else:
            y = self.odds.index(a)
            x = self.evens.index(b)
            print("robot played V:",x,y)
            return (y,x,"v")
    def end_game(self):
        self.ended = True


## MAIN EVENT LOOP

async def handler(websocket, path):
    logger.info("Start listening")
    game = None
    # msg = await websocket.recv()
    try:
        async for msg in websocket:
            logger.info("< {}".format(msg))
            try:
                msg = json.loads(msg)
            except json.decoder.JSONDecodeError as err:
                logger.error(err)
                return False
            game = msg["game"]
            answer = None
            if msg["type"] == "start":
                # Initialize game
                if msg["game"] in games:
                    games[msg["game"]].add_player(msg["player"])
                else:
                    nb_rows, nb_cols = msg["grid"]
                    games[msg["game"]] = agentclass(msg["player"],
                                                    nb_rows,
                                                    nb_cols,
                                                    msg["timelimit"])
                if msg["player"] == 1:
                    # Start the game
                    nm = games[game].next_action()
                    print('nm = {}'.format(nm))
                    if nm is None:
                        # Game over
                        logger.info("Game over")
                        continue
                    r, c, o = nm
                    answer = {
                        'type': 'action',
                        'location': [r, c],
                        'orientation': o
                    }
                else:
                    # Wait for the opponent
                    answer = None

            elif msg["type"] == "action":
                # An action has been played
                r, c = msg["location"]
                o = msg["orientation"]
                games[game].register_action(r, c, o, msg["player"])
                if msg["nextplayer"] in games[game].player:
                    # Compute your move
                    nm = games[game].next_action()
                    if nm is None:
                        # Game over
                        logger.info("Game over")
                        continue
                    nr, nc, no = nm
                    answer = {
                        'type': 'action',
                        'location': [nr, nc],
                        'orientation': no
                    }
                else:
                    answer = None

            elif msg["type"] == "end":
                # End the game
                games[msg["game"]].end_game()
                answer = None
            else:
                logger.error("Unknown message type:\n{}".format(msg))

            if answer is not None:
                print(answer)
                await websocket.send(json.dumps(answer))
                logger.info("> {}".format(answer))
    except websockets.exceptions.ConnectionClosed as err:
        logger.info("Connection closed")
    logger.info("Exit handler")


def start_server(port):
    server = websockets.serve(handler, 'localhost', port)
    print("Running on ws://127.0.0.1:{}".format(port))
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()


## COMMAND LINE INTERFACE

def main(argv=None):
    global agentclass
    parser = argparse.ArgumentParser(description='Start agent to play Dots and Boxes')
    parser.add_argument('--verbose', '-v', action='count', default=0, help='Verbose output')
    parser.add_argument('--quiet', '-q', action='count', default=0, help='Quiet output')
    parser.add_argument('port', metavar='PORT', type=int, help='Port to use for server')
    args = parser.parse_args(argv)

    logger.setLevel(max(logging.INFO - 10 * (args.verbose - args.quiet), logging.DEBUG))
    logger.addHandler(logging.StreamHandler(sys.stdout))

    agentclass = DotsAndBoxesAgent
    start_server(args.port)


if __name__ == "__main__":
    sys.exit(main())
