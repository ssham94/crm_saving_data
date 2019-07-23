from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    note = TextField()

    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        return f'{self.first_name} {self.last_name}'

    class Meta:
        database = db

db.connect()
db.create_tables([Contact])