# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class emp:
    empDict={}
    def __init__(self):
        self.id=0
        self.name=""
        self.type=""

    def getDetails(self,id):
        self.id = emp.empDict[id].id
        self.name = emp.empDict[id].name
        self.type = emp.empDict[id].type
        return

    @staticmethod
    def deleteEmp(id):
        if(id in emp.empDict.keys()):
            emp.empDict.pop(id)
            return True
        else:
            return False

    @staticmethod
    def checkId(id):
        if (id in emp.empDict.keys()):
            if(emp.empDict[id].type=="Director"):
                return dir()
            elif(emp.empDict[id].type=="Manager"):
                return mgr()
            elif(emp.empDict[id].type=="Technical Trainer"):
                return tt()
        else:
            return 0



class dir(emp):
    def __init__(self):
        self.share=0
        super().__init__()

    def add(self):
        if(self.id not in emp.empDict.keys()):
            emp.empDict[self.id]=self
            return True
        else:
            return False

    def getDetails(self,id):
        if(id in emp.empDict.keys()):
            super().getDetails(id)
            self.share=emp.empDict[id].share
            return
        else:
            return False


class mgr(emp):
    def __init__(self):
        self.incentive=0
        super().__init__()

    def add(self):
        if (self.id not in emp.empDict.keys()):
            emp.empDict[self.id] = self
            return True
        else:
            return False

    def getDetails(self,id):
        if (id in emp.empDict.keys()):
            super().getDetails(id)
            self.incentive = emp.empDict[id].incentive
            return
        else:
            return False

class tt(emp):
    def __init__(self):
        self.salary=0
        super().__init__()

    def add(self):
        if (self.id not in emp.empDict.keys()):
            emp.empDict[id] = self
            return True
        else:
            return False

    def getDetails(self,id):
        if (id in emp.empDict.keys()):
            super().getDetails(self,id)
            self.salary = emp.empDict[id].salary
            return
        else:
            return False
while(1):
    print("\n1.Add Employee\n2.Get Details\n3.Delete Employee\n4.Exit\n\n")
    c=int(input("Enter your choice : "))
    if(c==1):
        print("\n----1.Director\n----2.Manager\n----3.Technical Trainer\n\n")
        c1=input("Choice : ")
        if(c1=='1'):
            ob = dir()
            ob.id = int(input("Enter ID : "))
            ob.name = input("Enter Name : ")
            ob.type = "Director"
            ob.share = int(input("Enter Share : "))
            if(ob.add()):
                print("--Succesfully added--")
            else:
                print("--ERROR--")

        if (c1=='2'):
            ob = mgr()
            ob.id = int(input("Enter ID : "))
            ob.name = input("Enter Name : ")
            ob.type = "Manager"
            ob.incentive = int(input("Enter Incentive : "))
            if (ob.add()):
                print("--Succesfully added--")
            else:
                print("--ERROR--")

        if (c1=='3'):
            ob = tt()
            ob.id = int(input("Enter ID : "))
            ob.name = input("Enter Name : ")
            ob.type = "Technical Trainer"
            ob.salary = int(input("Enter Salary : "))
            if (ob.add()):
                print("--Succesfully added--")
            else:
                print("--ERROR--")


    elif(c==2):
        id=int(input("Enter ID : "))
        obj=emp.checkId(id)
        if(obj!=0):
            obj.getDetails(id)
            print("\n1.Employee ID : ",obj.id,"\n2.Employee Name : ",obj.name,"\n3.Employee Type : ",obj.type)
            if(obj.type=="Director"):
                print("4.Director's Share : ",obj.share)
            elif(obj.type=="Manager"):
                print("4.Manager's Incentive : ",obj.incentive)
            elif(obj.type=="Technical Trainer"):
                print("4.TT's Salary : ",obj.salary)
        else:
            print("--ERROR--")

    elif(c==3):
        id=int(input("\nEnter ID : "))

        if(emp.deleteEmp(id)):
            print("\nDeleted Succesfully\n")
        else:
            print("--ERROR--")

    elif(c==4):
        exit()

