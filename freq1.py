s="I think that I can make cool products really cool"

def freq(s):
    s2=[]
    s2=s.split()
    s3={}
    for item in s2:
        
        v=s2.count(item)
        s3.update({item:v})

    return s3
               





s1={}
s1=freq(s)
print(s1)
