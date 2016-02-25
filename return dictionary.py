list1=['first','last','location','education','work']

dict={'first':'Dipanjan','last':'Mantri','Visa':'F1','Major':'Software Engineering'}

def count(l,d):
    c=0
    for item in l:
        if item in d:
            c+=1

    return c



c1=count(list1,dict)
print(c1)

