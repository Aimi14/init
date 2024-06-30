from flask import jsonify, request, abort
from app import app
from app.database import get_db_connection, init_db

init_db()  # Initialize the database

@app.route('/funds', methods=['GET'])
def get_funds():
    conn = get_db_connection()
    funds = conn.execute('SELECT * FROM funds').fetchall()
    conn.close()
    return jsonify([dict(fund) for fund in funds])

@app.route('/funds', methods=['POST'])
def create_fund():
    if not request.json or not 'name' in request.json:
        abort(400)
    new_fund = {
        'name': request.json['name'],
        'manager_name': request.json.get('manager_name', ""),
        'description': request.json.get('description', ""),
        'nav': request.json.get('nav', 0),
        'date_of_creation': request.json.get('date_of_creation', ""),
        'performance': request.json.get('performance', 0)
    }
    conn = get_db_connection()
    conn.execute("INSERT INTO funds (name, manager_name, description, nav, date_of_creation, performance) VALUES (?, ?, ?, ?, ?, ?)",
                 (new_fund['name'], new_fund['manager_name'], new_fund['description'], new_fund['nav'], new_fund['date_of_creation'], new_fund['performance']))
    conn.commit()
    conn.close()
    return jsonify(new_fund), 201

@app.route('/funds/<int:fund_id>', methods=['GET'])
def get_fund(fund_id):
    conn = get_db_connection()
    fund = conn.execute('SELECT * FROM funds WHERE fund_id = ?', (fund_id,)).fetchone()
    conn.close()
    if fund is None:
        abort(404)
    return jsonify(dict(fund))

@app.route('/funds/<int:fund_id>', methods=['PUT'])
def update_fund(fund_id):
    if not request.json:
        abort(400)
    conn = get_db_connection()
    fund = conn.execute('SELECT * FROM funds WHERE fund_id = ?', (fund_id,)).fetchone()
    if fund is None:
        abort(404)
    updated_fund = {
        'performance': request.json.get('performance', fund['performance'])
    }
    conn.execute('UPDATE funds SET performance = ? WHERE fund_id = ?',
                 (updated_fund['performance'], fund_id))
    conn.commit()
    conn.close()
    return jsonify(updated_fund)

@app.route('/funds/<int:fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    conn = get_db_connection()
    fund = conn.execute('SELECT * FROM funds WHERE fund_id = ?', (fund_id,)).fetchone()
    if fund is None:
        abort(404)
    conn.execute('DELETE FROM funds WHERE fund_id = ?', (fund_id,))
    conn.commit()
    conn.close()
    return jsonify({'result': True})

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500