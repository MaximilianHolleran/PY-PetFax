from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
print(pets)
bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<pet_name>')
def pet_show(pet_name):
    pet = next((pet for pet in pets if pet['pet_name'] == pet_name), None)
    return render_template('show_pet.html', pet=pet )