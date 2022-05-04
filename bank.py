from flask import Flask, request, Response
from database.db import initialize_db
from database.models import User

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/bank'
}
initialize_db(app)


@app.route('/bank', methods=['POST'])
def open_account():
    body = request.get_json()
    user = User(**body).save()
    account = user.id
    return {'id': str(account)}, 200


@app.route('/bank/<id>', methods=['PUT'])
def update_balance(id):
    body = request.get_json()
    User.objects.get(id=id).update(**body)
    return '', 200


@app.route('/bank/<id>', methods=['DELETE'])
def delete_account(id):
    User.objects.get(id=id).delete()
    return '', 200


@app.route('/bank/<id>')
def get_account_details(id):
    movies = User.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run(debug=True)
