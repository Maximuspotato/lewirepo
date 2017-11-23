from flask import Flask, jsonify, request, abort
from app.models.user import User

lewis=User("mmm","jjj")
app = Flask(__name__)

"""users = [
    {
        'email': u'ricky@gmail.com',
        'password': u'pasword', 
        'done': False
    },
    {
        'email': u'trico@gmail.com',
        'password': u'pass', 
        'done': False
    }
]


#@app.route('/brightevents/api/v1.0/users', methods=['GET'])
#def get_users():
    #return jsonify({'users': users})

@app.route('/brightevents/api/v1.0/users', methods=['POST'])
def register_user():
    if not request.json or not 'email' in request.json:
        abort(400)
    user = {
        'email': request.json['email'],
        'password': request.json['password'],
        'done': False
    }
    users.append(user)
    return jsonify({'user': user}), 201"""

if __name__ == '__main__':
    app.run()