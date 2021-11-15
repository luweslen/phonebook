from tkinter import *
from controllers.controller import Controller

class View:
  def __init__(self, root):
    self.root = root
    self.form = {
      'container': None,
      '_id': None,
      'name': {
          'label': None,
          'value': None,
      },
      'phone': {
          'label': None,
          'value': None,
      },
      'type': {
          'label': None,
          'value': None,
      },
      'is_favorite': {
          'label': None,
          'value': None,
      },
      'button_save_and_update': None,
      'button_search_and_cancel': None
    }
    self.contacts = {
      'container': None,
      'label': None,
      'items': None
    }

    self.controller = Controller(self)
    self.setup_form_container()
    self.setup_contacts_container()

    self.controller.get_contacts()

  def setup_form_container(self):
    self.form['container'] = Frame(self.root)
    self.form['container'].grid()

    self.form['name']['label'] = Label(self.form['container'], text='Nome: ')
    self.form['name']['label'].grid(row=1, column=0)
    self.form['name']['value']  = Entry(self.form['container'])
    self.form['name']['value'].grid(row=1, column=1, columnspan=2, sticky=W+E)

    self.form['phone']['label'] = Label(self.form['container'], text='Telefone: ')
    self.form['phone']['label'].grid(row=2, column=0)
    self.form['phone']['value'] = Entry(self.form['container'])
    self.form['phone']['value'].grid(row=2, column=1, columnspan=2, sticky=W+E)

    self.form['type']['label'] = Label(self.form['container'], text='Tipo: ').grid(row=3, column=0)
    self.form['type']['value'] = StringVar()

    Radiobutton(self.form['container'], text='Comercial', width=20,
                variable=self.form['type']['value'], value='commercial',
                anchor=W).grid(column=1, row=3, padx=5, pady=5)

    Radiobutton(self.form['container'], text='Pessoal', width=20,
                variable=self.form['type']['value'],
                value='folks',
                anchor=W).grid(column=2, row=3, padx=5, pady=5)

    self.form['is_favorite']['label'] = Label(self.form['container'], text='Favorito? ').grid(row=4, column=0)
    self.form['is_favorite']['value'] = BooleanVar()

    Checkbutton(self.form['container'], text='Sim', width=20,
                variable=self.form['is_favorite']['value'], anchor=W).grid(row=4, column=1)
    self.buttons_container = Frame(self.root)
    self.buttons_container.grid()

    self.form['button_save_and_update'] = Button(
      self.form['container'],
      width=20,
      text="Salvar",
      command=self.controller.create_contact
    )
    self.form['button_save_and_update'].grid(row=6, column=2)

    self.form['button_search_and_cancel'] = Button(
      self.form['container'],
      width=20,
      text="Pesquisar",
      command=self.controller.search_contact
    )
    self.form['button_search_and_cancel'].grid(row=6, column=1)

  def setup_contacts_container(self):
    self.contacts['container'] = Frame(self.root)
    self.contacts['container'].grid()
    self.contacts['label'] = Label(self.contacts['container'], text='Contatos')
    self.contacts['label'].grid(row=8, column=0, columnspan=3, sticky=W+E)

    self.contacts['items'] = Frame(self.contacts['container'])
    self.contacts['items'].grid()

  def get_values_form(self):
    body = {
      'name': self.form['name']['value'].get(),
      'phone': self.form['phone']['value'].get(),
      'type': self.form['type']['value'].get(),
      'is_favorite': self.form['is_favorite']['value'].get()
    }

    return body

  def reset_form(self):
    self.form['button_save_and_update'].config(text="Salvar", command=self.controller.create_contact)
    self.form['button_search_and_cancel'].config(text="Pesquisar", command=self.controller.search_contact)

    self.form['name']['value'].delete(0, END)
    self.form['name']['value'].insert(0, "")
    self.form['phone']['value'].delete(0, END)
    self.form['phone']['value'].insert(0, "")

    self.form['type']['value'].set("commercial")
    self.form['is_favorite']['value'].set(False)

  def set_form(self, contact):
    self.form['button_save_and_update'].config(text="Atualizar", command=self.controller.update_contact)
    self.form['button_search_and_cancel'].config(text="Cancelar", command=self.reset_form)

    self.form['_id'] = contact['_id']
    self.form['name']['value'].delete(0, END)
    self.form['name']['value'].insert(0, contact['name'])
    self.form['phone']['value'].delete(0, END)
    self.form['phone']['value'].insert(0, contact['phone'])

    self.form['type']['value'].set(contact['type'])
    self.form['is_favorite']['value'].set(contact['is_favorite'])

  def reset_contacts(self):
    if not self.contacts['items'] == None:
      for widget in self.contacts['items'].winfo_children():
        widget.destroy()

  def set_contacts(self, contacts):
    self.reset_contacts()    

    base_row = 9
    count = 1

    for contact in contacts:
      current_row = base_row + count
      Label(self.contacts['items'], text=contact['name']).grid(row=current_row, column=0, sticky=E)
      Button(
        self.contacts['items'], 
        width=20,
        text="Detalhes",
        command= lambda contact = contact: self.controller.pre_update(contact)
      ).grid(row=current_row, column=1)

      Button(
        self.contacts['items'], 
        width=20,
        text="Excluir",
        command= lambda id = contact['_id']: self.controller.remove_contact(id)
      ).grid(row=current_row, column=2)
      count += 1
