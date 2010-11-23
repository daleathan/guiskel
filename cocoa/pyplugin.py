import objc
NSObject = objc.lookUpClass('NSObject')

from core.mainwindow import MainWindow
from core.textholder import TextHolder

class PyMainWindow(NSObject):
    def init(self):
        self = super(PyMainWindow, self).init()
        self.model = MainWindow()
        return self
    
    def setNameHolder_andMsgHolder_(self, nameHolder, msgHolder):
        self.model.set_children(nameHolder.model, msgHolder.model)
    
    def selectRandomName(self):
        self.model.select_random_name()
    
    def sayHello(self):
        self.model.say_hello()
    

class PyTextHolder(NSObject):
    def initWithView_(self, view):
        self = super(PyTextHolder, self).init()
        self.view = view
        self.model = TextHolder(view=self)
        return self
    
    def text(self):
        return self.model.text
    
    def setText_(self, newtext):
        self.model.text = newtext
    
    def update_text(self):
        self.view.updateText()
    
