from flask import (
    Blueprint, jsonify
)

from carrack.data.db import get_db

bp = Blueprint('victoria', __name__, url_prefix='/victoria')

@bp.route('/manifest')
def get_manifest():
    db = get_db()
    sm = db.execute('SELECT * FROM carracks WHERE name = ?', ('Victoria',)).fetchone()
    if sm:
        return jsonify({'name': sm['name'], 'capacity': sm['capacity']})
    else:
        return 'no such manifest', 404

@bp.route('/start-journey')
def start_journey():
    db = get_db()
    sm = db.execute('SELECT * FROM carracks WHERE name = ?', ('Victoria',)).fetchone()
    if sm:
        return 'The Victoria is already on a journey :D', 400
    else:
        db.execute('INSERT INTO carracks (name, capacity, status) VALUES (?, ?, ?)', ('Victoria', 2000, 1)).fetchone()
        return 'The Victoria has departed', 200