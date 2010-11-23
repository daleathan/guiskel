from PyQt4.QtCore import QObject

from core.textholder import TextHolder as TextHolderModel

class TextHolder(QObject):
    def __init__(self, view):
        QObject.__init__(self)
        self.view = view
        self.model = TextHolderModel(view=self)
    
    #--- model --> view
    def update_text(self):
        text = self.model.text
        if text != self.view.text():
            self.view.setText(text)
    
