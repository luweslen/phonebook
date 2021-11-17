from models.contact import Contact

class Controller:
  def __init__(self, View):
    self.model = Contact()
    self.view = View
    self.id = None

  def create_contact(self):
    try:
      body = self.view.get_values_form()
      self.model.create(body)

      self.view.show_messagebox('Contato adicionado com sucesso')
      self.view.reset_form()

      self.get_contacts()
    except ValueError as err:
      self.view.show_messagebox(str(err), type='showerror')

  def update_contact(self):
    try:
      body = self.view.get_values_form()
      self.model.update(self.id, body)

      self.view.show_messagebox('Contato atualizado com sucesso')
      self.view.reset_form()

      self.get_contacts()
    except ValueError as err:
      self.view.show_messagebox(str(err), type='showerror')

  def pre_update(self, contact):
    self.id = contact['_id']
    self.view.set_form(contact)

  def pre_remove(self, id, name):
    message = f'Certeza que deseja excluir {name} dos contatos'
    result = self.view.show_messagebox(message, type='askquestion')

    if result == 'yes':
      self.remove_contact(id)

  def remove_contact(self, id):
    try:
      self.model.remove(id)
      self.get_contacts()
    except ValueError as err:
      self.view.show_messagebox(str(err), type='showerror')

  def search_contact(self):
    body = self.view.get_values_form()

    params = {
      'name': body['name']
    }

    self.get_contacts(params)

  def get_contacts(self, params=None):
    contacts = self.model.get_all(params)

    if len(contacts) > 0:
      self.view.set_contacts(contacts)
    else:
      message = f'Não foi encontrado nenhum contato com este nome.'
      self.view.show_messagebox(message)

