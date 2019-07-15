#class account

class account:

    count=5600010

    def get(self):
        self.name=input("Name:")
        self.balance=int(input("Balance:"))
        
        
    def __init__(self):
        account.count+=1
        self.accno=account.count
        

    def display(self):
        print("****************************************")
        print("User Account Number:%d"%self.accno)
        print("User Name:%s"%self.name)
        print("User Balance:%d"%self.balance)
        

    def deposit(self,n):
        if(n<=0):
            print("invalid amount!")
        else:
            self.balance=self.balance+n

    def withdrawl(self,m):
        if(m<=0):
            print("invalid amount!")
        elif(self.balance-m<1000):
            print("Your minimum limit is 1000!")
        else:
            
            self.balance=self.balance-m



class fd(account):

    r=8
    def get(self):
        super().get()
        self.gender=input("Gender:")
        self.age=int(input("Age:"))
        self.time=int(input("Time for Fixed Deposit(in months):"))
    
    
        if self.gender=='f' and self.age<=55:
             print("Interest rate should be:%d"%self.r)
        elif self.gender=='f' and self.age>=55:
             fd.r+=1
        elif self.gender=='m' and self.age<=60:
             print("Interest rate should be:%d"%self.r)
        elif self.gender=='m' and self.age>=60:
             fd.r+=1
    
          
             
    def display(self):
         super().display()
         print("User Gender:%s"%self.gender)
         print("User Age:%s"%self.age)
         print("Time for Fixed Deposit:%d"%self.time)
         print("Interest rate of FD is:%d"%self.r)
         print("Maturaity Amount is :%d"%self.z)

    def maturaity(self):
        
            self.b=(self.r)/12
            self.z=(self.b)*(self.time)
         
    

def __main__():
    f=fd()
    ac=account()
    ac.get()
    ac.display()
    while(1):
        print("Account type:")
        print("1-Saving Account")
        print("2-Current Account")
        print("3-Fixed Deposit")
    
        t=int(input("Account Type:"))
        if t==1:
            a=ac.deposit(100)
            a=ac.withdrawl(100)
            a=ac.display()
            
            
            

        elif t==2:
             a=ac.deposit(100)
             a=ac.withdrawl(100)
             a=ac.display()
             
             
            
        elif t==3:
            a=f.get()
            a=f.maturaity()
            a=f.display()
            
        else:
            print("Invalid Option!")
        
        break
        
        
     

    
            
            

__main__()
    
    
