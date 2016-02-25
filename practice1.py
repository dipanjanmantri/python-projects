dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

list1=[]

def count(d,s):
    
    for item in d:
        list1.append(s.format(name=item['name'],food=item['food']))

    return list1

list2=[]
list2=count(dicts,string)
for item in list2:
    print(item)
        
