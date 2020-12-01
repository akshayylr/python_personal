import numpy as np


def winner_check(board):
    winner="none"
    winner_found=False
#    print(board)
    state=("O","X")
    for cha in state:
        for i in range(0,3):
            if board[i][0]==cha:
                if board[i][1]==cha:
                    if board[i][2]==cha:
                        winner_found=True
                        winner=cha
                       # print("row"+winner)
                        break
            if board[0][i]==cha:
                if board[1][i]==cha:
                    if board[2][i]==cha:
                        winner=cha
                        winner_found=True
                       # print("column"+winner)
                        break
            if board[0][0]==cha:
                if board[1][1]==cha:
                    if board[2][2]==cha:
                      winner=cha
                      winner_found=True
                     # print("r dia"+winner)
                      break
            if board[0][2]==cha:
                if board[1][1]==cha:
                    if board[2][0]==cha:
                        winner=cha
                        winner_found=True
                        #print("left dia"+winner)
                        break
    return winner,winner_found



def board_status_check(board):
    full=True
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==" ":
                full=False
                break
    return full


def user_input_position():
  inputs=["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
  while True:
      pos=input("enter a value corresponding to the given place: ")
      #print(pos)
      found=False
      for check in inputs:
          if check==pos:
              found=True
              break
          else:
              found=False
      if found:
          return int(pos)
      elif found:
          print("wrong entry")
          continue


def print_matrix(board):
    for i in range(0,3):
      print(str(3*i+1)+"  |"+str(3*i+2)+"  |"+str(3*i+3)+"   ")
      print(" "+str(board[i][0])+" | "+str(board[i][1])+" | "+str(board[i][2])+" ")
      print("   |   |   ")
      if i<2:
          print("------------")

def check_duplicate(pos,board):
   duplicate=False
   print("outside "+str(pos))
   if pos<4:
       print("less than 4")
       if board[0][pos-1]!=" ":
           duplicate=True
           print(duplicate)
   if pos in range(4,7):
       print("4 to 7")
       if board[1][pos-4]!=" ":
           duplicate=True
   elif pos>6:
       print("7+")
       if board[2][pos-7]!=" ":
           duplicate=True
   return duplicate



def xo_matrix_writer(inp,board):
    position =int(user_input_position())
    duplicate = check_duplicate(position, board)
    if not duplicate:
        if position<4:
            board[0][(position-1)]=inp
            write=True
        elif position in range(4,7):
            board[1][(position-4)]=inp
            write=True
        else:
            board[2][(position-7)]=inp
            write=True
    elif duplicate:
      #xo_matrix_writer(inp,board)
      print("position "+str(position)+" is already taken")
      write=False

    return write



replay=True
while replay:
    count = 0
    board = np.array([[" "," "," "], [" "," "," "],[" "," "," "]])
    board_full = False
    winner_found = False
    while not board_full and not winner_found :
    #print(board)
        if count%2==0 :
            print("its x's turn")
            write=xo_matrix_writer("X",board)
        else:
            print("its o turn")
            write= xo_matrix_writer("O",board)
        if write:
            count=count+1
        board_full=board_status_check(board)
        winner,winner_found = winner_check(board)
        print_matrix(board)
    print(winner + " is the winner!!!!!!")
    ye=(input("to replay click y else any button: "))
    if ye=="y":
        replay=True
        continue
    else:
        print("Thank you")
        replay=False
        continue
