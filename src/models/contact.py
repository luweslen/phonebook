from configs.database import database

class Contact:
  def __init__(self):
    self.database = database
    self.fields = ['name', 'phone', 'type', 'is_favorite']

  def valid_fields(self, body):
    for field in self.fields:
      if not field in body:
        raise ValueError(f'Unfilled field {field}')
    
    for field in self.fields:
      if type(body[field]) is str:
        if not body[field]:
          raise ValueError(f'Empty field {field}')

    if not body['phone'].isnumeric():
      raise ValueError(f'Phone invalid')

  def create(self, body):
    self.valid_fields(body)

    created_contact = self.database.contacts.insert_one(body)

    if created_contact.inserted_id:
      return 'Contact created successfully'
    else:
      return 'Error creating new contact'

  def update(self, id, body):
    self.valid_fields(body)

    updated_contact = self.database.contacts.update_one(
      { '_id': id },
      { '$set': body }
    )

    return updated_contact

  def remove(self, id):
    removed_contact = self.database.contacts.delete_one({'_id': id })
    return removed_contact

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
