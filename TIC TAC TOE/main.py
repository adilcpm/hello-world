#Function Defining

def disboard(board): #Used for displaying the board, takes a list as input
    print(f"\n|  {board[1]}  | |  {board[2]}  | |  {board[3]}  |\n-----------------------\n|  {board[4]}  | |  {board[5]}  | |  {board[6]}  |\n-----------------------\n|  {board[7]}  | |  {board[8]}  | |  {board[9]}  |\n")

def clrscr(): #Clears the screen by printing 100 lines
    print("\n"*100)

def takeinput(player,where): #Takes the players symbol and puts it on the corresponding place, the user chose
    mainboard[where]=player

def gamewin(board,last): #To check whether is the game is completed 
    global replay
    if board[1]!=" " and board[2]!=" " and board[3]!=" " and board[4]!=" " and board[5]!=" " and board[6]!=" " and board[7]!=" " and board[8]!=" " and board[9]!=" ":
        print("\n\n The board is full, no winners found !\n") #Check whether the board is full
        replay= input("Do you want to play again, Y to play again, N to stop the game : ").upper()
        return True

    if board[1]==board[2]==board[3]!=" " or board[4]==board[5]==board[6]!=" " or board[7]==board[8]==board[9]!=" " or board[1]==board[4]==board[7]!=" " or board[2]==board[5]==board[8]!=" " or board[3]==board[6]==board[9]!=" " or board[1]==board[5]==board[9]!=" " or board[7]==board[5]==board[3]!=" ":
        print(f"\n\n Congarulations ! {last} won the game\n") #Winner is found and prompt to play again
        replay= input("Do you want to play again, Y to play again, N to stop the game : ").upper()
        return True
    else:
        return False

#Main Code
clrscr()
replay=str
print("\nWelcome the the Best Tic TaY Toe Game Ever !\n") #Welcome Message
playing=input("Type Y for playing the game, N for exiting out : ").upper()

while playing=="Y":

    clrscr()
    print("--------Sample---------")
    sampleboard=['x',"1","2","3","4","5","6","7","8","9"] #Sample Board with numbers for the user the understand the order 
    disboard(sampleboard)
    player1=input("\nDo you want to be X or O ? :").upper() #Takes X or O as input
   
    if player1=="X":
        player2="O"
    else:
        player2="X"

    clrscr()
    mainboard=['x'," "," "," "," "," "," "," "," "," "]  #initializing with blank space
    disboard(mainboard)
    while True:
        where=int(input("\nPlayer 1 : Where do you want to place : ")) #input to take the number and run function to input it into board 
        takeinput(player1,where)                                       #and check whether game is completed
        clrscr()
        disboard(mainboard)
        if gamewin(mainboard,"Player 1"):
            break                                                       #Break out of while True loop
        where=int(input("\nPlayer 2 : Where do you want to place : "))
        takeinput(player2,where)
        clrscr()
        disboard(mainboard)
        if gamewin(mainboard,"Player 2"):
            break                                                       #Break out of while True loop
    if replay=="Y": #Used for exiting after the game is completed once
        continue    #skips the break down the line
    break           #breaks the loop completely
            
clrscr()
print("Thank you playing this game, hope you have a good day !")
    