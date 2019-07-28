import pymysql
class studentsi:
    
    def __init__(self,id,name,maths,hindi,english):
         self.id=id
         self.name=name
         self.maths=maths
         self.hindi=hindi
         self.english=english
         
    def avg(self):
        self.avg=(self.maths+self.hindi+self.english)/3;
        return self.avg
    def insert(self,avg):
        db=pymysql.connect("localhost","root","mysql","school")
        cobj=db.cursor()
        sql="insert into studentsi values ('%d','%s','%d','%d','%d','%d')"%(self.id,self.name,self.maths,self.hindi,self.english,avg)
        cobj.execute(sql)
        db.commit()
        
