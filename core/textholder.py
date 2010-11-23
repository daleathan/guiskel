
class TextHolder:
    def __init__(self, view):
        self.view = view
        self._text = ''
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, newtext):
        if newtext != self._text:
            self._text = newtext
            self.view.update_text()
    
