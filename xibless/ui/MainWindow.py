ownerclass = 'MainWindow'
ownerimport = 'MainWindow.h'

# Init
result = Window(400, 400, 318, 115, "guiskel")
nameLabel = Label(result, text="Name:")
nameLabel.width = 45
nameField = TextField(result, text="")
helloLabel = Label(result, text="")
helloButton = Button(result, title="Say Hello", action=Action(owner, 'sayHello'))
randomButton = Button(result, title="Random Name", action=Action(owner, 'randomName'))
randomButton.width = 119

# Owner Assignments
owner.nameTextField = nameField
owner.msgTextField = helloLabel

# Layout
nameLabel.packToCorner(Pack.UpperLeft)
nameField.packRelativeTo(nameLabel, Pack.Right, Pack.Middle)
nameField.fill(Pack.Right)
helloLabel.packRelativeTo(nameLabel, Pack.Below, Pack.Left)
helloLabel.fill(Pack.Right)
helloButton.packRelativeTo(helloLabel, Pack.Below, Pack.Right)
randomButton.packRelativeTo(helloButton, Pack.Left, Pack.Above)
nameField.setAnchor(Pack.UpperLeft, growX=True)
helloLabel.setAnchor(Pack.UpperLeft, growX=True)
helloButton.setAnchor(Pack.UpperRight)
randomButton.setAnchor(Pack.UpperRight)
