from tkinter import Tk
from views.View import View


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x400')
        self.root.title('Agenda Telefônica')

        View(self.root)

        self.root.mainloop()


App()
