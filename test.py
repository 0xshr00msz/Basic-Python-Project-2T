from DTR import Register   # From Register.py file Register Class
import datetime
import os

class TimeClock:
    def __init__(self):
        self.date = datetime.datetime.now()

    def reg(self):
        reg = input("Enter your name to register: ")
        return reg

    def time_in(self):
        reg = input('Enter your name to time in: ')
        return reg

    def time_out(self):
        reg = input('Enter your name to time out: ')
        return reg

    def run(self):
        while True:
            menu = input('Select your choice \n(1) Register\n(2) Time in\n(3) Time out\nEnter your Choice: ')
            if not menu.isdigit():
                print('Invalid input. Please enter a number between 1 and 3.')
                continue
            menu = int(menu)

            if menu == 1:
                file_handler = Register(self.reg() + ".txt")
                file_handler.write_to_file("")
            elif menu == 2:
                file_handler = Register(self.time_in() + ".txt")
                file_name = file_handler.file_name

                if os.path.exists(file_name):
                    file_handler.appendDate(self.date.strftime("%m") + "/" + self.date.strftime("%d") + "/" + self.date.strftime("%Y"))
                    file_handler.appendTimeIn(self.date.strftime("%I") +  ":" + self.date.strftime("%M") + self.date.strftime("%p"))
                else:
                    print('Employee does not exist. Please register your name.')
            elif menu == 3:
                file_handler = Register(self.time_out() + '.txt')
                file_name = file_handler.file_name

                if os.path.exists(file_name):
                    file_handler.appendTimeOut(self.date.strftime("%I") +  ":" + self.date.strftime("%M") + self.date.strftime("%p"))
                else:
                    print("Employee does not exist. Please register your name.")
                
            go_back = input('Do you want to go back to the menu? (y/n) ')
            if go_back.lower() == 'n':
                break

if __name__ == "__main__":
    time_clock = TimeClock()
    time_clock.run()
