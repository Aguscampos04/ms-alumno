from marshmallow import Schema, fields, post_load, validate
from app.models import Alumno

class AlumnoMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))
    apellido = fields.String(required=True, validate=validate.Length(min=1, max=50))
    nro_documento = fields.Integer(required=True, attribute="nrodocumento")
    tipo_documento = fields.String(required=True)
    sexo = fields.String(required=True, validate=validate.OneOf(["M", "F"]))
    nro_legajo = fields.Integer(required=True)
    especialidad_id = fields.Integer(required=True)

    @post_load
    def nuevo_alumno(self, data, **kwargs):
        return Alumno(**data)