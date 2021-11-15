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
      self.view.reset_form()
      self.get_contacts()
    except ValueError as err:
      print(str(err))

  def update_contact(self):
    try:
      body = self.view.get_values_form()
      self.model.update(self.id, body)
      self.view.reset_form()
      self.get_contacts()
    except ValueError as err:
      print(str(err))

  def pre_update(self, contact):
    self.id = contact['_id']
    self.view.set_form(contact)

  def remove_contact(self, id):
    self.model.remove(id)
    self.get_contacts()

  def search_contact(self):
    body = self.view.get_values_form()

    params = {
      'name': body['name']
    }

    self.get_contacts(params)

  def get_contacts(self, params=None):
    contacts = self.model.get_all(params)
    self.view.set_contacts(contacts) 
