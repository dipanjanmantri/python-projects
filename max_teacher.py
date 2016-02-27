dict1={'a':['history','Geography','Pol Sc','Math'],
       'b':['Spanish','Italian','Anthropology'],
       'c':['Symbolic systems','Data structures']}

def max_classes(dict):
    teacher=''
    max_count=0
    for x,y in dict.items():
        if len(y)>max_count:
            max_count=len(y)
            teacher=x
    return teacher

teacher=''
teacher=max_classes(dict1)
print(teacher)
