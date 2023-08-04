from flask import (
    Blueprint, jsonify
)
import string, random

from carrack.entity.cargo import Cargo, CargoSchema
from carrack.entity.cargo_type import CargoType

bp = Blueprint('santa_maria', __name__, url_prefix='/santa-maria')


cargos = [Cargo("Seed Money", 100000, 1)]

@bp.route("/cargo")
def get_manifest():
    schema = CargoSchema(many=True)
    return jsonify(schema.dump(cargos))

@bp.route("/cargo", methods = ['POST'])
def add_cargo():
    description = ''.join(random.choices(string.ascii_lowercase, k = 6))
    cargo = CargoSchema().load({
        "description": description,
        "amount": random.randint(1, 10),
        "type": random.randint(1, 3)})
    cargos.append(cargo)
    return '', 204
