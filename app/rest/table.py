from flask import Blueprint, jsonify

from app.models.models import Tipo, TipoSchema

table = Blueprint('table', __name__)

@table.route('/api/tipos')
def get_tables():
    tipos = Tipo.query.all()
    tipo_schema = TipoSchema()
    tipo_schema = TipoSchema(many=True)
    result = tipo_schema.dump(tipos)
    return jsonify({'success':True, 'data': result})

@table.route("/api/tipos/<id>")
def table_detail(id):
    tipo = Tipo.query.get(id)
    tipo_schema = TipoSchema()
    d = tipo_schema.dump(tipo) 
    return jsonify({'success':True, 'data': d})