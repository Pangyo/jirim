from peewee import *

db = SqliteDatabase('model.db')

class BaseModel(Model):
    class Meta:
        database = db

class NodeEntity(BaseModel):
    name = TextField(primary_key=True)
    title = TextField(null=False)
    link = TextField(null=False)
    infrom = TextField(null=True)
    
    class Meta:
        database = db # This model uses the "model.db" database.
