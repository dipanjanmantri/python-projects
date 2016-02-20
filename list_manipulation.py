shopping=[]

def options():
  print("Type done to quit, help to show this message, show to dispaly the items in the list :")
  
  
def show():
  print("The items in the list are: ")
  for item in shopping:
    print(item)
    
    
while(True):
  value=input("Type done to quit and display the items, show to display the items and help to show the options :")
  if value=="done":
    show()
    break
  elif value=="show":
    show()
    continue
  elif value=="help":
    options()
    continue
  else:
    
    items=input("enter the items :")
    list1=items.split(",")
    
    index=input("type the index :")
    val=int(index)
    if val==0:
      shopping.extend(list1)
    else:
      spot=val-1
      for item in list1:
        shopping.insert(spot,item)
        spot+=1
      
    
    
    
  
     
  
