from configs.database import database

class Contact:
  def __init__(self):
    self.database = database
    self.fields = ['name', 'phone', 'type', 'is_favorite']
    self.fields_pt_br = {
      'name': 'nome', 
      'phone': 'telefone', 
      'type': 'iipo', 
      'is_favorite': 'favorito'
    }

  def valid_fields(self, body):
    for field in self.fields:
      if not field in body:
        raise ValueError(f'Campo {self.fields_pt_br[field]} não enviado. Envie este campo e tente novamente.')
    
    for field in self.fields:
      if type(body[field]) is str:
        if not body[field]:
          raise ValueError(f'Campo {self.fields_pt_br[field]} está vazio. Preencha este campo e tente novamente.')

    if not body['phone'].isnumeric():
      raise ValueError(f'Campo telefone inválido. Digite apenas números nesse campo.')

  def create(self, body):
    self.valid_fields(body)

    created_contact = self.database.contacts.insert_one(body)

    if not created_contact.inserted_id:
      raise 'Erro ao criar um novo contato, tente novamente.'

  def update(self, id, body):
    self.valid_fields(body)

    updated_contact = self.database.contacts.update_one(
      { '_id': id },
      { '$set': body }
    )

    if updated_contact.modified_count < 1:
      raise 'Erro ao atualizar o contato, tente novamente.'

  def remove(self, id):
    removed_contact = self.database.contacts.delete_one({'_id': id })

    if removed_contact.deleted_count < 1:
      raise 'Erro ao deletar o contato, tente novamente.'

  def get_all(self, params = None):
    query = []

    if params:
      if 'name' in params:
        params['name'] = { '$regex': params['name'] }
        
      if 'phone' in params:
        params['phone'] = { '$regex': params['phone'] }
      query.append({ "$match": params })

    contacts = self.database.contacts.aggregate(query)

    return list(contacts)
