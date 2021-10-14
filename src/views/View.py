from tkinter import *


class View:
    def __init__(self, root):
        self.root = root
        self.setup_form_container()
        self.setup_buttons_container()
        self.setup_contacts_container()

    def setup_form_container(self):
        self.form_container = Frame(self.root).grid()

        Label(self.form_container, text='Nome: ').grid(row=1, column=0)
        self.name = Entry(self.form_container).grid(
            row=1, column=1, columnspan=2, sticky=W+E)

        Label(self.form_container, text='Telefone: ').grid(row=2, column=0)
        self.phone = Entry(self.form_container).grid(
            row=2, column=1, columnspan=2, sticky=W+E)

        Label(self.form_container, text='Tipo: ').grid(row=3, column=0)
        self.type = StringVar()

        Radiobutton(self.form_container, text='Comercial', width=20,
                    variable=self.type, value='terror',
                    anchor=W).grid(column=1, row=3, padx=5, pady=5)

        Radiobutton(self.form_container, text='Pessoal', width=20,
                    variable=self.type,
                    value='computação',
                    anchor=W).grid(column=2, row=3, padx=5, pady=5)

        Label(self.form_container, text='Favorito? ').grid(row=4, column=0)
        self.is_favorite = BooleanVar()

        Checkbutton(self.form_container, text='Sim', width=20,
                    variable=self.is_favorite, anchor=W).grid(row=4, column=1)

    def setup_buttons_container(self):
        self.buttons_container = Frame(self.root).grid()

        Button(self.buttons_container, width=20,
               text="Buscar").grid(row=6, column=0)
        Button(self.buttons_container, width=20,
               text="Salvar").grid(row=6, column=1)
        Button(self.buttons_container, width=20,
               text="Excluir").grid(row=6, column=2)

    def setup_contacts_container(self):
        self.contacts_container = Frame(self.root).grid()
        Label(self.contacts_container, text='Nenhum contato registrado').grid(
            row=7, column=0, columnspan=3, sticky=W+E)
