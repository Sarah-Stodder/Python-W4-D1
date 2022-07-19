from datetime import datetime as dt
#Parent class:
class User():
    def __init__(self, first_name, last_name,email,):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.time_stamp = dt.utcnow()
      
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self):
         return f'<User | {self.full_name} {self.time_stamp}>'

    def __repr__(self):
        return f'<user | {self.last_name} {self.time_stamp}>'

    def __lt__(self, __o):
        return self.time_stamp < __o.time_stamp
    
   
    
  
#first name [string]
#last name [string]
#email [string]
#created_on [time stamp]


#child one:
#home_address [string]
#security_level [int]
#department [string]
#id - which is made by taking the employee's full_name concatenating it with their department
class Employee(User):
    def __init__(self, home_address, security_level, department, first_name, last_name, email,):
        super().__init__(first_name, last_name, email)
        self.home_address = home_address
        self.security_level = security_level
        self.department = department
      
#change their first name
#change their last name
#change their department
    @property
    def id(self):
        return self.first_name + '.' + self.last_name + '.' + self.department

    
    def describe(self):
        return print(f" User's Name: {self.full_name},\nThey work in {self.department}, \nTheir clearence is {self.security_level},\nAccount created {self.time_stamp} \n{self.id}")

sarah = Employee("124 fake street", 6,"Marketing","Sarah","Stodder", "sjsarahboo@gmail.com")
sarah.describe()



#child two:
#shipping_address [string]
#billing_address [string]
#purchase_history [list]
#id - which is made by taking the customers email and concatenating it with their shipping adress
class Customer(User):
    def __init__(self, billing_address, purchase_history, first_name, last_name, email,shipping_address):
        super().__init__(first_name, last_name, email)
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.purchase_history = purchase_history
    @property
    def id(self):
        return print(self.email + self.shipping_address)

    def describe(self):
        return print(f"User: {self.full_name},\nAccount Email: {self.email}, \npurchase History: {self.purchase_history} \nShipping address: {self.shipping_address},\nBilling Address: {self.billing_address},\nAccount created: {self.time_stamp} \n{self.id}")

sheldon = Customer("123 fake street",["tooth paste", "gummy worms", "soda"],"Sheldon","stodder","fake@email.com","123 fake street")
sheldon.describe()






#Employees can:
#change their first name
#change their last name
#change their department
sarah.first_name = "Haras"
print(sarah.full_name)
sarah.last_name = "Red dots"
print(sarah.full_name)
sarah.department = "CFO"
sarah.describe()
print("="*20)


#change their first name
#change their last name
#change their billing_address
#change their shipping_address
sheldon.first_name = "shellybean"
print(sheldon.full_name)
sheldon.last_name = "reddots"
print(sheldon.full_name)
sheldon.shipping_address = "5309 new street"
sheldon.billing_address = sheldon.shipping_address
sheldon.describe()
print("="*20)

