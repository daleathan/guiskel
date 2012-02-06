import sys

from gi.repository import Gtk
from gtk.mainwindow import MainWindow

def main(argv):
    mw = MainWindow()
    mw.show_all()
    return Gtk.main()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
