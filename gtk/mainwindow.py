from gi.repository import Gtk

from core.mainwindow import MainWindow as MainWindowModel
from .textholder import TextHolder
from .lineedit import LineEdit

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="guiskel")
        self._setupUi()
        self.model = MainWindowModel()
        self.nameEntry = LineEdit(view=self.nameEntryView)
        self.helloLabel = TextHolder(view=self.helloLabelView)
        self.model.set_children(self.nameEntry.model, self.helloLabel.model)
        self.randomNameButton.connect('clicked', self.randomNameButtonClicked)
        self.sayHelloButton.connect('clicked', self.sayHelloButtonClicked)
        self.connect('delete-event', Gtk.main_quit)
    
    def _setupUi(self):
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)
        self.nameEntryView = Gtk.Entry()
        self.box.pack_start(self.nameEntryView, False, False, 0)
        self.helloLabelView = Gtk.Label()
        self.box.pack_start(self.helloLabelView, False, False, 0)
        self.buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.randomNameButton = Gtk.Button(label="Random Name")
        self.sayHelloButton = Gtk.Button(label="Say Hello")
        self.buttonBox.pack_end(self.sayHelloButton, False, False, 0)
        self.buttonBox.pack_end(self.randomNameButton, False, False, 0)
        self.box.pack_start(self.buttonBox, False, False, 0)
    
    def randomNameButtonClicked(self, widget):
        self.model.select_random_name()
    
    def sayHelloButtonClicked(self, widget):
        self.model.say_hello()

