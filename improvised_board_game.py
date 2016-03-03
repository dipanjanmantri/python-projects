import random

cells=[(0,0),(0,1),(0,2),
       (1,0),(1,1),(1,2),
       (2,0),(2,1),(2,2)]

def locations():
    start=random.choice(cells)
    monster=random.choice(cells)
    door=random.choice(cells)
    
   # if start==monster or start==door or door==monster:
    #    return locations()
    
    return start,monster,door


def move_player(player,move):
    x,y=player
    if move=='LEFT':
        y-=1
    if move=='RIGHT':
        y+=1
    if move=='UP':
        x-=1
    if move=='DOWN':
        x+=1
    

    return x,y


def get_moves(player):
    moves=['LEFT','RIGHT','UP','DOWN']
    if player[1]==0:
        moves.remove('LEFT')
    if player[1]==2:
        moves.remove('RIGHT')
    if player[0]==0:
        moves.remove('UP')
    if player[0]==2:
        moves.remove('DOWN')
    
        
    return moves



    
    
    



def draw_matrix(player):
    print(" _ _ _")
    border="|{}"
    for index,cell in enumerate(cells):
        if index in [0,1,3,4,6,7]:
            if cell==player:
                print(border.format("X"),end='')
            else:
                print(border.format("_"),end='')
        else:
            if cell==player:
                print(border.format("X|"))
            else:
                print(border.format("_|"))
                

player,monster,door=locations()

while(True):
    moves=get_moves(player)
    print("welcome to the dungeon")
    print("currently you are in {} room".format(player))
    draw_matrix(player)
    print("you can move {}".format(moves))
    print("enter QUIT to quit")
    move=input(">")
    move=move.upper()
   
    if move=="QUIT":
        break
    if move in moves:
        player=move_player(player,move)
        
    
    elif player==door:
        print("you win")
        break
    elif player==monster:
        print("you were eaten by the monster")
        break
    else:
        print("you cant move further")
        continue
    
        


