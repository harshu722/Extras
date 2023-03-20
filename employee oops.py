class Employee:
    id = 10
    name = "john"
    def display(self):
      print("ID: %d \nName: %s"%(self.id,self.name))
#Creating a emp instance of employee class
emp = Employee()
emp.display()
