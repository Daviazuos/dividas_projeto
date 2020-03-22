import jwt
from flask import Flask
import os
import datetime
import time

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/logintest',methods=['POST','GET'])
def EncodeAuthToken(UserId):
    d = datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=1)
    e = datetime.datetime.utcnow()
    try:
        Payload = {
            'exp': time.mktime(d.timetuple()),
            'GenerationTokenTime':time.mktime(e.timetuple()) ,
            'UserId' : UserId
        }
        return jwt.encode(
            Payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['UserId']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def test_encode_auth_token():
    user = {
        'email':'test@test.com',
        'password':'test'
    }
    auth_token = EncodeAuthToken(user)
    UserId = decode_auth_token(auth_token)
    return UserId

tete = test_encode_auth_token()

if __name__ == '__main__':
    app.run(debug=True)