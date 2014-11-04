import httplib

from flask import Flask, request, make_response, jsonify

from co import factory, errors

app = Flask('Co App')
users_service = factory.create_users_service()

@app.route('/users', methods=['POST'])
def register_user():
    try:
        users_service.register(request.json['nickname'])
        return jsonify(), httplib.CREATED
    except errors.UserAlreadyRegisteredError:
        return jsonify({'error': 'Nickname already taken'}), httplib.CONFLICT


@app.route('/users/<nickname>/following', methods=['GET', 'POST'])
def following_users(nickname):
    if request.method == 'GET':
        try:
            following = users_service.follows_to(nickname)
            print following
            return jsonify({'result': following}), httplib.OK
        except errors.UserDoesNotExistError:
            return jsonify({'error': 'User does not exist'}), httplib.NOT_FOUND

    if request.method == 'POST':
        try:
            following = users_service.follow_to(nickname, request.json['nickname'])
            return jsonify(), httplib.CREATED
        except errors.UserDoesNotExistError:
            return jsonify({'error': 'User does not exist'}), httplib.NOT_FOUND


if __name__ == '__main__':
    app.run(debug=True)
