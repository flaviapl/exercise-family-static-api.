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
    response_body = members
    
    return jsonify(response_body), 200


@app.route('/member/<int:id>', methods=['GET'])
def get_single_member(id):

    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404


@app.route('/member', methods=['POST'])
def add_member():
    print(request.get_json())
    # print(request.get_json()["first_name"])
    data = request.get_json()

    new_member = jackson_family.add_member(data)

    return jsonify(new_member), 200



@app.route('/member/<int:id>', methods=['DELETE'])
def delete_single_member(id):

    member_to_delete = jackson_family.delete_member(id)
    if member_to_delete :
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
