import json


def addToChildren(nodes,value):
    for node in nodes:
        node['parentPlays'] = value
        plays = node['plays']
        print(node)
        if node['children'] != []:
            print('added')
            addToChildren(node['children'],plays)


file = open('tree.data')
tree = json.loads(file.read())
for node in tree['nodes']:
    plays = node['plays']
    print(node)
    if node['children'] != []:
        print('added')
        addToChildren(node['children'],plays)
file.close()
with open('tree.data', 'w') as outfile:
    json.dump(tree, outfile)
