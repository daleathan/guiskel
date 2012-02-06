from .textholder import TextHolder

class LineEdit(TextHolder):
    def __init__(self, view):
        TextHolder.__init__(self, view)
        self.view.connect('changed', self.handleTextEdited)
    
    def handleTextEdited(self, widget):
        self.model.text = self.view.get_text()
    
