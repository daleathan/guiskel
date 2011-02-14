from tkinter import Frame, Label, Entry, Button, StringVar

from core.mainwindow import MainWindow as MainWindowModel
from core.textholder import TextHolder as TextHolderModel

class LabelTextHolder(Label):
    def __init__(self, master=None):
        Label.__init__(self, master)
        self.model = TextHolderModel(view=self)
    
    #--- model --> view
    def update_text(self):
        text = self.model.text
        if text != self['text']:
            self['text'] = text


class EntryTextHolder(Entry):
    def __init__(self, master=None):
        Entry.__init__(self, master)
        self._value = StringVar()
        self['textvariable'] = self._value
        self._value.trace('w', self._valuechanged)
        self.model = TextHolderModel(view=self)
    
    def _valuechanged(self, *args):
        self.model.text = self._value.get()
    
    #--- model --> view
    def update_text(self):
        text = self.model.text
        if text != self.get():
            self.delete(0, 'end')
            self.insert(0, text)
    

class MainWindow(Frame):
    def createWidgets(self):
        self.nameLabel = Label(self, text="What's your name:")
        self.nameLabel.pack(side='top')
        
        self.nameInput = EntryTextHolder(self)
        self.nameInput.pack(side='top', fill='x', expand=True)
        
        self.helloLabel = LabelTextHolder(self)
        self.helloLabel.pack(side='top')
        
        self.sayHelloButton = Button(self, text="Say Hello")
        self.sayHelloButton.pack(side='right')
        self.sayHelloButton['command'] = self.model.say_hello
        
        self.randomNameButton = Button(self, text="Random Name")
        self.randomNameButton.pack(side='right')
        self.randomNameButton['command'] = self.model.select_random_name
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.model = MainWindowModel()        
        self.pack()
        self.createWidgets()
        self.model.set_children(self.nameInput.model, self.helloLabel.model)
        
    
