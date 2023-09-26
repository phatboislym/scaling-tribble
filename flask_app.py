from flask import Flask, request
import jwt

app = Flask(__name__)

# Secret key for token generation and validation (keep it secret!)
SECRET_KEY = 'mysecretkey'


def authenticate(username, password):
    # Verify username and password (dummy implementation)
    if username == 'user' and password == 'password':
        return True
    return False


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if authenticate(username, password):
        # Generate a token
        token = jwt.encode({'username': username},
                           SECRET_KEY, algorithm='HS256')
        return {'token': token}
    else:
        return {'error': 'Authentication failed'}, 401


@app.route('/protected', methods=['GET'])
def protected_resource():
    token = request.headers.get('Authorization').split()[1]

    try:
        # Verify and decode the token
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return {'message': 'Access granted for user: ' + decoded['username']}
    except jwt.ExpiredSignatureError:
        return {'error': 'Token has expired'}, 401
    except jwt.DecodeError:
        return {'error': 'Token is invalid'}, 401


if __name__ == '__main__':
    app.run(debug=True)

