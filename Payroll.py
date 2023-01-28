from datetime import datetime   #use the datetime module to detect hours and minutes

class Payroll:
    def __init__(self, name, rate): #initialize the parameters
        self.name = name
        self.rate = rate
    
    def calculatePay(self, arrival, departure):        #method to calculate the pay
        hours = (departure - arrival).seconds / 3600    #use .seconds rather than hour to convert the minutes to decimal
        pay = 0                                         #divide by 3600 to convert to an integer hour
        if hours > 8:                                   #use to calculate for overtime pay
            pay = 8 * self.rate
            overtimeHours = hours - 8
            overtimePay = overtimeHours * self.rate * 1.25
            pay += overtimePay
        else:
            pay = hours * self.rate
        return pay                                      

def main():
    name = input("Enter employee name: ")
    employee = Payroll(name, 10)
    while True:
        try:
            arrival = input("Enter arrival time (HH:MM): ")
            departure = input("Enter departure time (HH:MM): ")
            arrival = datetime.strptime(arrival, "%H:%M")           #use the %H:%M to not return an error when inputing 08:00, but accept it
            departure = datetime.strptime(departure, "%H:%M")       #%H:%M is a format used in the strptime function, expecting 24 hour format
            break
        except ValueError:
            print("Invalid input. Please enter the time in the format HH:MM")
    pay = employee.calculatePay(arrival, departure)
    print("Pay for", employee.name, "is $", pay)

if __name__ == "__main__":
    main()
