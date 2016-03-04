class Name:
    val1=45
    val2="second value"
    score=2,5
    def __init__(self,**access):
        self.name=access.get('val1','Sam')
        self.height=access.get('val2',6.2)
        self.weight=access.get('val3',80)
        self.preference=access.get('val4','Biryani')
        for key,value in access.items():
            setattr(self,key,value)
        
def __str__(self):
    return "The individual values are {} and {}".format(self.val1,self.val2)
        
class subName(Name):
    val3=88
    val4='devops engineer'
    val1=99
    val2='within subclass'

class subName1(Name):
    val1='within subName1'
    val2='also within subName1'
