from flask import Flask, jsonify, request
import string, random

from model.santa_maria import Cargo, CargoSchema
from model.cargo_type import CargoType

app = Flask(__name__)



cargos = [Cargo("Seed Money", 100000, 1)]

@app.route("/")
def hello_world():
    return "hello"

@app.route("/cargo")
def get_manifest():
    schema = CargoSchema(many=True)
    return jsonify(schema.dump(cargos))

@app.route("/cargo", methods = ['POST'])
def add_cargo():
    description = ''.join(random.choices(string.ascii_lowercase, k = 6))
    cargo = CargoSchema().load({
        "description": description,
        "amount": random.randint(1, 10),
        "type": random.randint(1, 3)})
    cargos.append(cargo)
    return '', 204
