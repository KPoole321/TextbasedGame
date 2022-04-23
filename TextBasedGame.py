#Kevin Poole | 04/17/2022 | IT-140-H7679

#Begining instructions, when called before main it will show the following:
def intro():
    print('Welcome to the Dungeons and Dragons Game!')
    print('Collect all 6 ring fragments to gain the strength to defeat the Dragon Slayer!')
    print('If you enter the dungeon before you have all the ring fragments, you will be defeated in combat! ')
    print('Move Commands: North, South, West, East, Exit.')
    print('In order to pick up the ring fragments you must enter: "Get RF" followed by the number.')
    print('For example: "Get RF2", would put ring fragment 2 in your bag.')
    print('If you enter the move "Exit" the game will end.')
    print('-' * 25)

#When calling on the main function the game will run.
def main():

    # The dictionary links a room to other rooms and the items they contain.
    rooms = {
        'Entrance': {'West': 'Kitchen'},
        'Kitchen': {'East': 'Entrance', 'South': 'Dining Hall', 'item': 'RF1'},
        'Dining Hall': {'South': 'King\'s Chamber', 'North': 'Kitchen', 'West': 'Dungeon',
                        'East': 'Armory', 'item': 'RF2'},
        'Dungeon': {'item': 'Dragon Slayer'},
        'Armory': {'West': 'Dining Hall', 'North': 'Barracks', 'item': 'RF5'},
        'Barracks': {'South': 'Armory', 'item': 'RF6'},
        'King\'s Chamber': {'North': 'Dining Hall', 'East': 'Guest Bedroom', 'item': 'RF3'},
        'Guest Bedroom': {'West': 'King\'s Chamber', 'item': 'RF4'},
        'Exit': {}
    }

    #This will return the item found in the room or it will return the prompt claiming there is no item here.
    def get_item(CurrentRoom):
        if 'item' in rooms[CurrentRoom]:
            return rooms[CurrentRoom]['item']
        if 'item' not in rooms[CurrentRoom]:
            return 'There is no item here.'

    #This function updates the current room the user is in.
    #By checking for the room with the correct move and returning the updated room given the inputted direction.
    def InNewRoom(CurrentRoom, Move):
        NewRoom = CurrentRoom
        for x in rooms:
            if x == CurrentRoom:
                if Move in rooms[x]:
                    NewRoom = rooms[x][Move]
        return NewRoom

    #Player starts at the Entrance.
    CurrentRoom = 'Entrance'

    #Create an empty inventory to store items.
    inventory = []

    #This loop will cover all possible solutions to a players input. Valid or invalid.
    while (CurrentRoom):
        #This is the continual prompt the player will see after every input/move.
        print('You are in {}'.format(CurrentRoom))
        print('Inventory: ', inventory)
        print('-' * 25)

        #This will check the item being returned from the previous definition 'get_item'.
        item = get_item(CurrentRoom)

        #The if statements will check the item in the room and see what available responses are necessary.
        #If the item in the room isn't the final boss (dragon slayer) than it will proceed.
        if item != 'Dragon Slayer':
            if CurrentRoom == 'Entrance':
                print('There are no items in this room')
            if CurrentRoom != 'Entrance':
                if item in inventory:
                    print('You current have this item in your inventory.')
                #Will prompt the player about the newfound item and prompt for input.
                else:
                    print('You found {}. Pick up this item!'.format(item))
                    PickupItem = input('Enter your move: ')
                    #This 'upper' function will allow redundancy if the player doesn't use caps in picking up the item.
                    PickupItem = PickupItem.upper()
                    if PickupItem == str('GET ' + item):
                        inventory.append(item)
                        print('You picked up {}!'.format(item))
                    if PickupItem == 'EXIT':
                        print('I hope you enjoyed the game!')
                        print('Gooodbye.')
                        break
                    if PickupItem != str('GET ' + item):
                        print('Sorry, try that command again.')

        #The player enters the room with the Dragon slayer with all 6 items than the loop will break congratulating them on winning!
        if item == 'Dragon Slayer':
            if len(inventory) == 6:
                print('You have successfully gathered all the ring fragments!')
                print('With the combined strength of the ring you managed to defeat the Dragon Slayer!')
                print('Congrats on your victory! Thank you for playing!')
                break
            #The player enters the room with the Dragon Slayer without all 6 items, then the player will lose.
            if len(inventory) != 6:
                print('You failed to collect all the ring fragments and were not strong enough to defeat the Dragon Slayer!')
                print('You have been defeated!')
                print('Thank you for playing!')
                break

        #This input will check for direction and provide redundancy by auto capitalizing the first letter.
        Move = input('Enter your move: ')
        Move = Move.title()

        #If the player types Exit the game will end, breaking the loop.
        if Move == 'Exit':
            print('I hope you enjoyed the game!')
            print('Gooodbye.')
            break

        #Checking to see if the input is any of the following directions followed by updating the current room the user is in.
        if (Move == 'North' or Move == 'South' or Move == 'West' or Move == 'East'):
            NewRoom = InNewRoom(CurrentRoom, Move)
            if NewRoom == CurrentRoom:
                print('Sorry! You can\'t go that way.')
            else:
                CurrentRoom = NewRoom
        else:
            print('Sorry! You can\'t go that way.')

intro()
main()
