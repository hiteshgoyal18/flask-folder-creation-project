from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from flask_rest_jsonapi import ResourceList
from flask_project.app.views import db, Person

class PersonSchema(Schema):
    class Meta:
        type_ = 'person'
        self_view = 'person_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'person_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str(required=True, load_only=True)
    email = fields.Email(load_only=True)
    birth_date = fields.Date
    display_name = fields.Function(lambda obj: "{} {}".format(obj.name.upper(), obj.email))
    computers = fields.Relationship(self_view='person_computers',
                                    self_view_kwargs={'id': '<id>'},
                                    related_view='computer_list',
                                    related_view_kwargs={'id': '<id>'},
                                    many=True,
                                    schema='ComputerSchema',
                                    type_='computer'
                                    )


class ComputerSchema(Schema):
    class Meta:
        type_ = 'computer'
        self_view = 'computer_detail'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Integer(as_string=True, dump_only=True)
    serial = fields.Str(required=True)
    owner = Relationship(attribute='person',
                         self_view='computer_person',
                         self_view_kwargs={'id': '<id>'},
                         related_view='person_detail',
                         related_view_kwargs={'computer_id': '<id>'},
                         schema='PersonSchema',
                         type_='person')



#create Resource Managers
class PersonList(ResourceList):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person}


