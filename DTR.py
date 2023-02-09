import csv

class Register:
    def __init__(self, file_name):
        self.file_name = file_name

    # Override everything in txt file
    # Used to initiate registration of employees
    def write_to_file(self, text):
        with open(self.file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time In", "Time Out"])
    # append date for Time In
    def appendDate(self, text):
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([text, '', ''])
    # append time for Time In
    def appendTimeIn(self, text):
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i, row in enumerate(rows):
                if len(row) < 3:
                    continue
                if row[1] == '':
                    rows[i][1] = text
                    break
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    # append time for Time Out
    def appendTimeOut(self, text):
        with open(self.file_name, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i, row in enumerate(rows):
                if len(row) < 3:
                    continue
                if row[2] == '':
                    rows[i][2] = text
                    break
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
