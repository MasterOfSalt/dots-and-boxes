import json
import csv

# game = {}
# game['player1'] = 'V1'
# game['player2'] = 'V2'
# game['player1_win'] = 202
# game['player2_win'] = 1
# game['dimensions'] = '4X4'
allgames = []
#allgames['player1vsplayer24x4'] = game



with open('../data/data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        added = False
        for game in allgames:
            if game['id'] == str(row[0])+" - "+str(row[1])+" - "+str(row[3]):
                if row[0] == row[2]:
                    game['player1_win'] += 1
                else:
                    game['player2_win'] += 1
                added = True
        if not added:
                game = {}
                game['id'] = str(row[0])+" - "+str(row[1])+" - "+str(row[3])
                game['player1'] = row[0]
                game['player2'] = row[1]
                if row[0] == row[2]:
                    game['player1_win'] = 1
                    game['player2_win'] = 0
                    game['dimensions'] = row[3]
                else:
                    game['player1_win'] = 0
                    game['player2_win'] = 1
                    game['dimensions'] = row[3]
                allgames.append(game)
                
with open('../data/parsedgames.json', 'w') as outfile:
    json.dump(allgames, outfile)
