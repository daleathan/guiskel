from tkinter import Tk
from tk.mainwindow import MainWindow

root = Tk()
app = MainWindow(master=root)
app.mainloop()
root.destroy()