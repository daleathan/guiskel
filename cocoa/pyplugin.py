from objp.util import pyref

from core.mainwindow import MainWindow
from core.textholder import TextHolder

class PyMainWindow:
    def __init__(self):
        self.model = MainWindow()
    
    def setNameHolder_andMsgHolder_(self, nameHolder: pyref, msgHolder: pyref):
        self.model.set_children(nameHolder.model, msgHolder.model)
    
    def selectRandomName(self):
        self.model.select_random_name()
    
    def sayHello(self):
        self.model.say_hello()
    

class TextHolderView:
    def updateText(self): pass

class PyTextHolder:
    def __init__(self, view: pyref):
        self.view = view
        self.model = TextHolder(view=self)
    
    def text(self) -> str:
        return self.model.text
    
    def setText_(self, newtext: str):
        self.model.text = newtext
    
    def update_text(self):
        self.view.updateText()
    
