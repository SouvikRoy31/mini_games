rooms = {
            'Hall' : {
                    'south' : 'Kitchen',
                    'east'  : 'Dining Room',
                    'item'  : 'key'
            },
            'Kitchen' : {
                    'north' : 'Hall',
                    'item'  : 'monster'
            },
            'Dining Room' : {
                    'west' : 'Hall',
                    'item' : 'potion',
                    'south': 'Garden'
            },
            'Garden' :{
                    'north' : 'Dining Room'
            }

        }
def showInstr():
    print('''
    RPG Game
    =======================================

    Get to the Garden with a key and a potion
    Avoid the monsters!

    Commands:
        go [direction]
        get [item]
        ''')
if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    {
    print('A monster has got you..... GAME OVER!')
    }

if currentRoom=='Garden' and 'key' in inventory and 'potion' in inventory:
    {
    print('You escaped the house..... You Win')
    }

currentRoom = 'Hall'
