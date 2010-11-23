from PyQt4.QtCore import QCoreApplication
from PyQt4.QtGui import (QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton,
    QLabel)

from core.mainwindow import MainWindow as MainWindowModel

from .textholder import TextHolder
from .lineedit import LineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self._setupUi()
        self.model = MainWindowModel()
        self.nameTextBox = LineEdit(view=self.nameTextBoxView)
        self.helloLabel = TextHolder(view=self.helloLabelView)
        self.model.set_children(self.nameTextBox.model, self.helloLabel.model)
        self.randomNameButton.clicked.connect(self.model.select_random_name)
        self.sayHelloButton.clicked.connect(self.model.say_hello)
    
    def _setupUi(self):
        self.setWindowTitle(QCoreApplication.instance().applicationName())
        self.centralwidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.nameTextBoxView = QLineEdit(self.centralwidget)
        self.verticalLayout.addWidget(self.nameTextBoxView)
        self.helloLabelView = QLabel(self.centralwidget)
        self.verticalLayout.addWidget(self.helloLabelView)
        self.buttonLayout = QHBoxLayout()
        self.randomNameButton = QPushButton("Random Name", self.centralwidget)
        self.buttonLayout.addWidget(self.randomNameButton)
        self.sayHelloButton = QPushButton("Say Hello", self.centralwidget)
        self.buttonLayout.addWidget(self.sayHelloButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        self.setCentralWidget(self.centralwidget)
    
