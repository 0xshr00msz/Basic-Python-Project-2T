
class Register:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, 'r') as file:
            return file.read()
    # Override everything in txt file
    # Used to initiate registration of employees
    def write_to_file(self, text):
        with open(self.file_name, 'w') as file:
            file.write(text)
    # append date for Time In
    def appendDate(self, text):
        with open(self.file_name, 'a') as file:
            file.write("\n" + text)
    # append time for Time In
    def appendTimeIn(self, text):
        with open(self.file_name, 'a') as file:
            file.write(" " + text)
    # append time for Time Out
    def appendTimeOut(self, text):
        with open(self.file_name, 'a') as file:
            file.write(" " + text)
    