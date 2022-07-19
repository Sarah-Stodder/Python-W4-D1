#Create 3 Instances of Employee and Customer
#Create a List of all your created users and have them sorted by creation date 
#Newest Users first using (.sort or sorted) 
#without a key (lambda function)

from homework import *
from time import sleep

anakin = Employee("123 tatooine way", 0, "Padwan","anakin","skywalker","ihatesand@gmail.com")
anakin.describe()
print("="*100)
sleep(2)
kylo = Employee("starkiller base",8,"Supreme leader", "Kylo", "Ren", "joinme@gmail.com")
kylo.describe()
print("="*100)
sleep(2)
yoda= Employee("456 dagoba place", 10, "Jedi Master", "yoda", "unknown", "thereisno_try@gmail.com")
yoda.describe()
print("="*100)
sleep(2)
#============================================================================================================

jamie= Customer("123 outlander street",["flowers","muskett pellets","whiskey"],"james","frazier","red_baron@gmail.com","123 outlander street")
jamie.describe()
print("="*100)
sleep(2)

dustin = Customer("555 hawkins street", ["16gb usb drive","gummy worms", "dice set"], "dustin", "Henderson", "dustybun@gmail.com", "473 hawkins way")
dustin.describe()
print("="*100)
sleep(2)
jack = Customer("777 black pearl street",["whiskey","dirt","swords"],"Jack","Sparrow","priateslife_forme@gmail.com","909 rum island")
jack.describe()
print("="*100)



users = [anakin, kylo, yoda, jamie, dustin, jack]
newest =sorted(users, reverse=True)
print(newest)

