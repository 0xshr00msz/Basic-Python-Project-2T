# Daily Time Record Class

from datetime import datetime   #use the datetime module to detect hours and minutes

class Payroll:
    def __init__(self, name, rate): #initialize the parameters
        self.name = name
        self.rate = rate
    
    def calculate_pay(self, arrival, departure):        #method to calculate the pay
        hours = (departure - arrival).seconds / 3600    #use .seconds rather than hour to convert the minutes to decimal
        pay = hours * self.rate                         #if .seconds 09:30 will be 9.5, while .hours will be 9 only
        return pay                                      #divide by 3600 to convert to an integer hour

name = input("Enter employee name: ")
employee = Payroll(name, 10)
arrival = input("Enter arrival time (HH:MM): ")
departure = input("Enter departure time (HH:MM): ")
arrival = datetime.strptime(arrival, "%H:%M")           #use the %H:%M to not return an error when inputing 08:00, but accept it
departure = datetime.strptime(departure, "%H:%M")       #%H:%M is a format used in the strptime function, expecting 24 hour format
pay = employee.calculate_pay(arrival, departure)
print("Pay for", employee.name, "is $", pay)
