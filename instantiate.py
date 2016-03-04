class Instantiate:
    def get_values(self):
        value1=input("please input either of a, b or c : ")
        if value1 in 'abc':
            if value1=='a':
                print("the alphabet is a")
            elif value1=='b':
                print("The alphabet is b")
            else:
                print("The alphabet is c")
        else:
            self.get_values()

    def __init__(self,**acess):
        self.values=self.get_values()
        
        
            
        
