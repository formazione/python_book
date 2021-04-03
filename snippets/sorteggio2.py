from random import shuffle
import ctypes  # An included library with Python install.   

# Global variables with students and days for test
c5ce = "Acone Battagliese Borrelli Carracino Ciardi"
days5ce = "3nov 5nov"
day5ce = days5ce.split()


class Show_random_list:

    def __init__(self, classe, day):
        self.classe = classe
        self.day = day
    
    def init(self):
        "Create the counter for students group and the day of test for each group"
        global counter, dayc

        counter = 0
        dayc = 0

    def shuffle_list(self):
        "Shuffle students order"
        global s

        s = self.classe.split()
        shuffle(s)
    
    def pp(self, d):
        "Print day of test"
        print(d)
        print("========")

    def show_list(self):
        "Show students and day of test with pp(...)"
        global s, counter, dayc

        self.pp(self.day[0])
        message = self.day[0]
        message += "\n"
        for n in s:
            print(n)
            counter += 1
            message += n
            message += "\n"
            if counter == 4:
                print()
                message += "\n"
                dayc +=1
                self.pp(self.day[dayc])
                message += self.day[dayc]
                message += "\n"
        ctypes.windll.user32.MessageBoxW(0, message, "Verifiche", 1)

    def functions_order(self):
        "Order of flow chart for the script"
        self.init()
        self.shuffle_list()
        self.show_list()
    
    def start_script(self):
        "Launch the functions in the right order"
        self.functions_order()

    # start_script()


l = Show_random_list(c5ce, day5ce)
l.start_script()
