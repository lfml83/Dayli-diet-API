from flask import Flask, request, jsonify
from models.diet import Diet
from database import db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'

db.init_app(app)



@app.route('/diet', methods = ["POST"])
def create_dite():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    inside_outside = data.get('inside_outside')
    print(inside_outside)

    if name:
        
        diet = Diet(name=name,description=description,inside_outside=inside_outside)
        db.session.add(diet)
        db.session.commit()
        return jsonify({"message" : "Dieta cadastrada com sucesso"})
    
    return jsonify({"message" : "Dados incorretos"}), 400# bad request, dados invalidos



@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True)