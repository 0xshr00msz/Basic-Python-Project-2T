from DTR import Register   # From Register.py file Register Class
import datetime
import os

date = datetime.datetime.now()
newDate = datetime.datetime(2022, 1, 29)

def reg():
    reg = input("Enter your name to register: ")
    return reg
def timeIn():
    reg = input('Enter your name to time in: ')
    return reg
def timeOut():
    reg = input('Enter your name to time out: ')
    return reg

menu = int(input('Select your choice \n(1) Register\n(2)Time in\n(3)Time out\nEnter your Choice: '))

if menu == 1:
    fileHandler = Register(reg() + ".txt")
    fileHandler.write_to_file("")
if menu == 2:
    fileHandler = Register(timeIn() + ".txt")
    filePath = 'FileHandling'
    fileName = fileHandler.file_name
    
    if os.path.exists(fileName):
        fileHandler.appendDate(date.strftime("%m") + "/" + date.strftime("%d") + "/" + date.strftime("%Y"))
        fileHandler.appendTimeIn(date.strftime("%I") +  ":" + date.strftime("%M") + date.strftime("%p"))
    else: 
        print('Employee does not exist. Please register your name.')
elif menu == 3:
    fileHandler = Register(timeOut() + '.txt')
    filePath = filePath = 'FileHandling'
    fileName = fileHandler.file_name

    if os.path.exists(fileName):
        fileHandler.appendTimeOut(date.strftime("%I") +  ":" + date.strftime("%M") + date.strftime("%p"))
    else:
        print("Employee does not exist. Please register your name.")

