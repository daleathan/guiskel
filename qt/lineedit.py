from .textholder import TextHolder

class LineEdit(TextHolder):
    def __init__(self, view):
        TextHolder.__init__(self, view)
        self.view.textEdited.connect(self.handleTextEdited)
    
    def handleTextEdited(self, newtext):
        self.model.text = newtext
    
