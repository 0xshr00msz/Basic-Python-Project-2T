from DTR import Register   # From Register.py file Register Class
from Payroll import Payroll
import datetime
import os

class ReadFile:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.time_in_data = {}

    def reg(self):
        reg = input("Enter your name to register: ")
        return reg

    def timeIn(self):
        reg = input('Enter your name to time in: ')
        self.time_in_data[reg] = self.date
        return reg

    def timeOut(self):
        reg = input('Enter your name to time out: ')
        return reg

    def main(self):
        while True:
            menu = input('Select your choice \n(1) Register\n(2) Time in\n(3) Time out\n(4) Calculate Pay\n(5) Exit the Terminal\nEnter your Choice: ')
            if not menu.isdigit():
                print('Invalid input. Please enter a number between 1 and 5.')
                continue
            menu = int(menu)

            if menu == 1:
                os.system('cls')
                fileHandler = Register(self.reg() + ".csv")
                fileHandler.write_to_file("")
            elif menu == 2:
                os.system('cls')
                name = self.timeIn()
                fileHandler = Register(name + ".csv")
                if os.path.exists(fileHandler.file_name):
                    fileHandler.appendDate(self.date.strftime("%m") + "/" + self.date.strftime("%d") + "/" + self.date.strftime("%Y"))
                    fileHandler.appendTimeIn(self.date.strftime("%H") +  ":" + self.date.strftime("%M"))
                else:
                    print('Employee does not exist. Please register your name.')
            elif menu == 3:
                os.system('cls')
                name = self.timeOut()
                if name:
                    fileHandler = Register(name + '.csv')
                    if os.path.exists(fileHandler.file_name):
                        fileHandler.appendTimeOut(self.date.strftime("%H") +  ":" + self.date.strftime("%M"))
                    else:
                        print("Employee does not exist. Please register your name.")
            elif menu == 4:
                os.system('cls')
                file_name = input("Enter the name of the Employee: ")
                register = Payroll(file_name)
                register.read()
            elif menu == 5:
                os.system('cls')
                print("Thank you for your service.\n")
                break

            while True:
                goBack = input('Do you want to go back to the menu? (y/n) ')
                if goBack.lower() == 'n':
                    os.system('cls')
                    print("Thank you for your service.\n")
                    exit()
                elif goBack.lower() == 'y':
                    os.system('cls')
                    break
                else:
                    print("Only input Y/y or N/n")
