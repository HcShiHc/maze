
game = False
coin = 0

#asking if the user would like to start the game   
start= input("Welcome! Do you Want to start the game? [y/n]")
if start == ("y"):
    game = True
    character = input("Input the symbol you want for your character: ")#user is allowed to choose how their character looks like
    wall = input("Input a symbol you want for your wall: ") #user is allowed to input symbol for wal
    characterX = 0
    characterY = 1
    print("")
    print("-------------------------------------")
    print("your character is "+character)
    print(wall+" is the wall. You are not allowed to go onto the walls. ")
    print("If you run into any of the walls, you will get sent back to your starting position.")
    print("Try to get the coins'$'to unlock larger maps.")
elif start == (""):
    game = True
    character = input("Input the symbol you want for your character: ")#user is allowed to choose how their character looks like
    wall = input("Input a symbol you want for your wall: ") #user is allowed to input symbol for wall
    characterX = 0
    characterY = 1
    print("")
    print("-------------------------------------")
    print("your character is "+character)
    print(wall+" is the wall. You are not allowed to go onto the walls. ")
    print("If you run into any of the walls, you will get sent back to your starting position.")
    print("Try to get the coins'$'to unlock larger maps.")
else:
    game = False 
    print("OK bye")

#this is the original array
myArray=[wall," ",wall,wall,wall,wall,wall,wall,wall,wall],[wall," "," "," "," ",wall," "," ","$",wall],[wall," "," "," "," ","$"," ",wall,wall,wall],[wall," "," "," "," ",wall," "," ",wall,wall],[wall,wall," "," "," "," "," "," ","$",wall],[wall,wall,wall," ",wall," "," "," "," ",wall],[wall,"$",wall," ",wall," "," "," ",wall,wall],[wall," "," "," ",wall," "," ",wall,wall,wall],[wall," "," ","$",wall," ","$",wall,wall,wall],[wall," ",wall,wall,wall,wall,wall,wall,wall,wall]


#This is the first gird of the game
def printGrid(): 
    print(str(myArray[0][0]) +str(myArray[0][1])+str(myArray[0][2])+str(myArray[0][3])+str(myArray[0][4])+str(myArray[0][5])+str(myArray[0][6]) +str(myArray[0][7])+str(myArray[0][8])+str(myArray[0][9]))
    print(str(myArray[1][0]) +str(myArray[1][1])+str(myArray[1][2])+str(myArray[1][3])+str(myArray[1][4])+str(myArray[1][5])+str(myArray[1][6]) +str(myArray[1][7])+str(myArray[1][8])+str(myArray[1][9]))
    print(str(myArray[2][0]) +str(myArray[2][1])+str(myArray[2][2])+str(myArray[2][3])+str(myArray[2][4])+str(myArray[2][5])+str(myArray[2][6]) +str(myArray[2][7])+str(myArray[2][8])+str(myArray[2][9]))
    print(str(myArray[3][0]) +str(myArray[3][1])+str(myArray[3][2])+str(myArray[3][3])+str(myArray[3][4])+str(myArray[3][5])+str(myArray[3][6]) +str(myArray[3][7])+str(myArray[3][8])+str(myArray[3][9]))
    print(str(myArray[4][0]) +str(myArray[4][1])+str(myArray[4][2])+str(myArray[4][3])+str(myArray[4][4])+str(myArray[4][5])+str(myArray[4][6]) +str(myArray[4][7])+str(myArray[4][8])+str(myArray[4][9]))
    print(str(myArray[5][0]) +str(myArray[5][1])+str(myArray[5][2])+str(myArray[5][3])+str(myArray[5][4])+str(myArray[5][5])+str(myArray[5][6]) +str(myArray[5][7])+str(myArray[5][8])+str(myArray[5][9]))
    print(str(myArray[6][0]) +str(myArray[6][1])+str(myArray[6][2])+str(myArray[6][3])+str(myArray[6][4])+str(myArray[6][5])+str(myArray[6][6]) +str(myArray[6][7])+str(myArray[6][8])+str(myArray[6][9]))
    print(str(myArray[7][0]) +str(myArray[7][1])+str(myArray[7][2])+str(myArray[7][3])+str(myArray[7][4])+str(myArray[7][5])+str(myArray[7][6]) +str(myArray[7][7])+str(myArray[7][8])+str(myArray[7][9]))
    print(str(myArray[8][0]) +str(myArray[8][1])+str(myArray[8][2])+str(myArray[8][3])+str(myArray[8][4])+str(myArray[8][5])+str(myArray[8][6]) +str(myArray[8][7])+str(myArray[8][8])+str(myArray[8][9]))
    print(str(myArray[9][0]) +str(myArray[9][1])+str(myArray[9][2])+str(myArray[9][3])+str(myArray[9][4])+str(myArray[9][5])+str(myArray[9][6]) +str(myArray[9][7])+str(myArray[9][8])+str(myArray[9][9]))


def movement(character):
    global characterX
    global characterY
    global coin
    move = int(input("start you moves: (use your number keys on keyboard to move): "))
    #For character to move left
    if (move == 2):
        myArray[characterX][characterY] = " "
        characterX = characterX+0
        characterY = characterY+1
        
        #if the position in array is empty/free for character to move 
        if(myArray[characterX][characterY] == " "):
            myArray[characterX][characterY] = character
            print(character) #character sets in position
        
        #if position in array is wall, it cannot move to the walls
        elif (myArray[characterX][characterY] == wall):
            character = myArray[0][1]
            print(character)
            print("You cannot go on the walls, You have been sent back to the starting point.")
        
        elif (myArray[characterX][characterY] == "$"): #collecting coins
            coin = coin + 1
            print("You have "+ str(coin) + " coins.")
        
    
    elif (move == 4):
        myArray[characterX][characterY] = " "
        characterX = characterX-1
        characterY = characterY+0
        
        if (myArray[characterX][characterY] == " "):
            myArray[characterX][characterY] = character
            print(character)
        
        elif (myArray[characterX][characterY] == wall):
            character = myArray[0][1]
            print(character)
            print("You cannot go on the walls, You have been sent back to the starting point.")
        
        elif (myArray[characterX][characterY] == "$"):
            coin = coin + 1
            print("You have "+ str(coin) + " coins.")
        
    
    elif (move == 8):
        myArray[characterX][characterY] = " "
        characterX = characterX+0
        characterY = characterY-1
        
        if (myArray[characterX][characterY] == " "):
            myArray[characterX][characterY] = character
            print(character)
        
        elif (myArray[characterX][characterY] == wall):
            characterX = 0
            characterY = 1
            myArray[characterX][characterY] = character
            print(character)
            print("You cannot go on the walls, You have been sent back to the starting point.")
        
        elif (myArray[characterX][characterY] == "$"):
            coin = coin + 1
            print("You have "+ str(coin) + " coins.")
        
    
    elif (move == 6):
        myArray[characterX][characterY] = " "
        characterX = characterX+1
        characterY = characterY+0
        
        if (myArray[characterX][characterY] == " "):
            myArray[characterX][characterY] = character
            print(character)
        
        elif (myArray[characterX][characterY] == wall):
            characterX = 0
            characterY = 1
            myArray[characterX][characterY] = character
            print(character)
            print("You cannot go on the walls, You have been sent back to the starting point.")
        
        elif (myArray[characterX][characterY] == "$"):
            coin = coin + 1
            print("You have "+ str(coin) + " coins.")
        
            
    
    
    elif (move == 1):
        myArray[characterX][characterY] = " "
        characterX = characterX-1
        characterY = characterY+1
        
        if (myArray[characterX][characterY] == " "):
            myArray[characterX][characterY] = character
            print(character)
        
        elif (myArray[characterX][characterY] == wall):
            characterX = 0
            characterY = 1
            myArray[characterX][characterY] = character
            print(character)
            print("You cannot go on the walls, You have been sent back to the starting point.")
                
        elif (myArray[characterX][characterY] == "$"):
            coin = coin + 1
            print("You have "+ str(coin) + " coins.")
        
           
    elif (move == 3):
        myArray[characterX][characterY] = " "
        characterX = characterX+1
        characterY = characterY+1
        
        if (myArray[characterX][characterY] == " "):
            myArray[characterX][characterY] = character
            print(character)
        
        elif (myArray[characterX][characterY] == wall):
            characterX = 0
            characterY = 1
            myArray[characterX][characterY] = character
            print(character)
            print("You cannot go on the walls, You have been sent back to the starting point.")
        
        elif (myArray[characterX][characterY] == "$"):
            coin = coin + 1
            print("You have "+ str(coin) + " coins.")
        
            
    elif (move == 7):
        myArray[characterX][characterY] = " "
        characterX = characterX-1
        characterY = characterY-1
        
        if (myArray[characterX][characterY] == " "):
            myArray[characterX][characterY] = character
            print(character)
        
        elif (myArray[characterX][characterY] == wall):
            characterX = 0
            characterY = 1
            myArray[characterX][characterY] = character
            print(character)
            print("You cannot go on the walls, You have been sent back to the starting point.")
        
        elif (myArray[characterX][characterY] == "$"):
            coin = coin + 1
            print("You have "+ str(coin) + " coins.")
    
    
    elif (move == 9):
        myArray[characterX][characterY] = " "
        characterX = characterX+1
        characterY = characterY-1
        
        if (myArray[characterX][characterY] == " "):
            myArray[characterX][characterY] = character
            print(character)
        
        elif (myArray[characterX][characterY] == wall):
            characterX = 0
            characterY = 1
            myArray[characterX][characterY] = character
            print(character)
            print("You cannot go on the walls, You have been sent back to the starting point.")
        
        elif (myArray[characterX][characterY] == "$"):
            coin = coin + 1
            print("You have "+ str(coin) + " coins.")
        

print("-------------------------------------")
while (game == True): #loop where the game starts
    myArray[characterX][characterY]=character #starting position
    printGrid()
    movement(character)
    
    print("-------------------------------------")
    
    if(myArray[characterX][characterY] == myArray[9][1]):
        print("Congrats you have reached the end of the game!")
        print("-------------------------------------")
        Cost= input("would you like to spend 10 game coins to unlock the bigger map? [y/n]")
        if (Cost == "y"):
            if (int(coin) < 5):
                print("")
                print("You don't have enough of coins, you need to pay 1000ft to unlock the next map.")
                print("You can pay at YEAR 11 Sisi.")
                print("")
        else:
            game = False
            print("Ok bye")
   
   
   
   

