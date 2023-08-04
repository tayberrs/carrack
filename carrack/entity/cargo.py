import datetime
from marshmallow import Schema, fields

class Cargo(object):
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.type = type
        self.created_at = datetime.datetime.utcnow()
    
    def __repr__(self):
        return '<Cargo(name={self.description!r})>'.format(self=self)

class CargoSchema(Schema):
    description = fields.Str()
    amount = fields.Integer()
    created_at = fields.DateTime()
    type = fields.Integer()