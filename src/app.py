"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")


#    + id: Int
#    + first_name: String
#    + last_name: String (Siempre Jackson)
#    + age: Int > 0
#    + lucky_numbers: Array of int

# Miembros iniciales de la familia
#John Jackson
#33 Years old
#Lucky Numbers: 7, 13, 22

#Jane Jackson
#35 Years old
#Lucky Numbers: 10, 14, 3

#Jimmy Jackson
#5 Years old
#Lucky Numbers: 1



John = jackson_family.add_member(member={
    'first_name': 'John',
    'age': 33,
    'id': 1,
    'lucky_numbers': [7, 13, 22]
})

Jane = jackson_family.add_member(member={
    'first_name': 'Jane',
    'age': 35,
    'id': 2,
    'lucky_numbers': [10, 14, 3]
})

Jimmy = jackson_family.add_member(member={
    'first_name': 'Jimmy',
    'age': 5,
    'id': 3,
    'lucky_numbers': [1]
})



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()


    return jsonify(members), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
