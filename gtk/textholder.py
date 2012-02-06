from core.textholder import TextHolder as TextHolderModel

class TextHolder:
    def __init__(self, view):
        self.view = view
        self.model = TextHolderModel(view=self)
    
    #--- model --> view
    def update_text(self):
        text = self.model.text
        if text != self.view.get_text():
            self.view.set_text(text)
    
