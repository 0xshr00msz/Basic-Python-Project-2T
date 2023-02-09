import csv
import datetime

class Payroll:
    def __init__(self, file_name):
        self.file_name = file_name
    def read(self):
        file_name = self.file_name + ".csv"
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            row_count = 0
            for row in reader:
                row_count += 1
                if row_count == 3:
                    time_in = row[1]
                if row_count == 3:
                    time_out = row[2]
                    break
            time_in = datetime.datetime.strptime(time_in, '%H:%M')
            time_out = datetime.datetime.strptime(time_out, '%H:%M')
            time_diff = (time_out - time_in).seconds / 3600

            pay = 0
            workingHours = 8
            amountPerHour = 93.75
            overtimeRate = 1.25

            if time_diff > 8:
                pay = workingHours * amountPerHour
                overtimeHours = time_diff - workingHours
                overtimePay = overtimeHours * amountPerHour * overtimeRate
                pay += overtimePay
            else:
                pay = time_diff * amountPerHour
            print("The pay for " + self.file_name + " is ₱" + str(pay))