from tkinter import Tk, PhotoImage
from views.View import View

class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x400')
        self.root.title('Agenda Telefônica')

        self.root.iconphoto(False, PhotoImage(file = './src/assets/icon.png'))

        View(self.root)

        self.root.mainloop()

App()
