import random

class MainWindow:
    def set_children(self, namebox, hellolabel):
        self.namebox = namebox
        self.hellolabel = hellolabel
    
    def say_hello(self):
        name = self.namebox.text
        msg = "Hello {}!".format(name)
        self.hellolabel.text = msg
    
    def select_random_name(self):
        CHOICES = ["Virgil", "World", "Luke Skywalker", "Vincent Vega", "Hannah Arendt"]
        name = random.choice(CHOICES)
        self.namebox.text = name
    
