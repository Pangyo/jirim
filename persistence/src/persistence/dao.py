from peewee import *

db = SqliteDatabase('model.db')

class Person(Model):
    name = CharField()

    class Meta:
        database = db # This model uses the "model.db" database.