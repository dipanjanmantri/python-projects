#create a list of fruits
#guess a random fruit from the list
#draw spaces 
#take guesses
#draw guessed letters and strikes
#print out win/lose

import random

fruit_list=[]
while(True):
  value=input("Yes or no :")
  if value=='n':
    break
  else:
    fruit=input("enter fruits :")
    fruit_list.append(fruit)


pick_fruit=random.choice(fruit_list)
good=[]
#convert_into_list=list(pick_fruit)
length=len(pick_fruit)
while(True):
  letter=input("guess a letter :")
  
    
  
  
  if letter in pick_fruit:
    
    
    good.append(letter)
    
  if len(good)==length:
    print("you win")
    print(pick_fruit)
    break
    
  for alphabet in good:
    print(alphabet)
  
  print()
    
  
  
  
    
    
  
