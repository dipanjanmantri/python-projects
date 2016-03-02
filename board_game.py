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
    x,y=start
    if move=='LEFT':
        x-=1
    if move=='RIGHT':
        x+=1
    if move=='UP':
        y-=1
    if move=='DOWN':
        y+=1
    

    return x,y


def get_moves(player):
    moves=['LEFT','RIGHT','UP','DOWN']
    if player[0]==0:
        moves.remove('LEFT')
    if player[0]==2:
        moves.remove('RIGHT')
    if player[1]==0:
        moves.remove('UP')
    if player[1]==2:
        moves.remove('DOWN')
        
    return moves

start,monster,door=locations()

    
    
    
player=start

while(True):
    moves=get_moves(player)
    print("welcome to the dungeon")
    print("currently you are in {} room".format(player))
    print("you can move {}".format(moves))
    print("enter QUIT to quit")
    move=input(">")
    move=move.upper()
    if move=="QUIT":
        break
    if move in moves:
        player=move_player(player,move)
    else:
        print("you cant move further")
        continue
    if player==door:
        print("you win")
        break
    if player==monster:
        print("you were eaten by the monster")
        break
    
        


