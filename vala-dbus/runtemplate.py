import dbus.service
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject

from core.mainwindow import MainWindow
from core.textholder import TextHolder

PROGID = 'org.hardcodedsoftware.guiskel'

class DEntryPoint(dbus.service.Object):
    IFACE_NAME = PROGID + '.EntryPoint'
    
    def __init__(self):
        session_bus = dbus.SessionBus()
        name = dbus.service.BusName(PROGID, session_bus)
        dbus.service.Object.__init__(self, name, '/entry')
        self.windows = []
    
    @dbus.service.method(IFACE_NAME, out_signature='s')
    def NewMainWindow(self):
        index = len(self.windows)
        object_path = '/window/%d' % index
        window = DMainWindow(object_path)
        self.windows.append(window)
        print(object_path)
        return object_path
    
class DMainWindow(dbus.service.Object):
    IFACE_NAME = PROGID + '.MainWindow'
    def __init__(self, object_path):
        session_bus = dbus.SessionBus()
        name = dbus.service.BusName(PROGID, session_bus)
        dbus.service.Object.__init__(self, name, object_path)
        self.object_path = object_path
        self.model = MainWindow()
        self.namebox = DTextHolder(self.NameboxPath())
        self.hellolabel = DTextHolder(self.HellolabelPath())
        self.model.set_children(self.namebox.model, self.hellolabel.model)
    
    @dbus.service.method(IFACE_NAME, out_signature='s')
    def NameboxPath(self):
        return self.object_path + '/namebox'
    
    @dbus.service.method(IFACE_NAME, out_signature='s')
    def HellolabelPath(self):
        return self.object_path + '/hellolabel'
    
    @dbus.service.method(IFACE_NAME)
    def SayHello(self):
        self.model.say_hello()
    
    @dbus.service.method(IFACE_NAME)
    def SelectRandomName(self):
        self.model.select_random_name()
    

class DTextHolder(dbus.service.Object):
    IFACE_NAME = PROGID + '.TextHolder'
    def __init__(self, object_path):
        session_bus = dbus.SessionBus()
        name = dbus.service.BusName(PROGID, session_bus)
        dbus.service.Object.__init__(self, name, object_path)
        self.object_path = object_path
        self.model = TextHolder(self)
    
    @dbus.service.method(IFACE_NAME, out_signature='s')
    def Text(self):
        return self.model.text
    
    @dbus.service.method(IFACE_NAME, in_signature='s')
    def SetText(self, text):
        self.model.text = text
    
    #--- Signals
    @dbus.service.signal(IFACE_NAME)
    def UpdateText(self):
        pass
    
    #--- Callbacks
    def update_text(self):
        self.UpdateText()

def main():
    DBusGMainLoop(set_as_default=True)
    entry = DEntryPoint()
    mainloop = GObject.MainLoop()
    print("DBus server running")
    print("Now, what you have to do is to run the 'guiskel' executable in vala-dbus/build.")
    mainloop.run()

if __name__ == '__main__':
    main()
