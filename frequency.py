s="I you I you me"

def dict(s):
    s1={}
    c=0
    c1=0
    s2=[]
    s3=[]
    s3=s.split()
    for item in s3:
        v=s3.count(item)
        s1.update({item:v})

    return s1


s4={}
s4=dict(s)
print(s4)
