from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from sqlalchemy.ext.declarative import DeclarativeMeta
import json 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ortonrko10@localhost/assignment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15))
    email = db.Column(db.String(100))
    salary = db.Column(db.Float)
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    department = db.Column(db.String(50))
    role = db.Column(db.String(50))


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id}), 201

def user_serializer(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data)
                fields[field] = data
            except TypeError:
                fields[field] = None
        return fields

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user_serializer(user))

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'user deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
    
    
# {
#     "name": "Naresh Vaishnav",
#     "mobile": "8879734967",
#     "email": "naresh123@gmail.com",
#     "salary": 80000,
#     "city": "Mumbai",
#     "country": "India",
#     "department": "Web Development",
#     "role": "Backend Developer"
# }