from flask import ( Blueprint, render_template, request )

bp = Blueprint('submit', __name__, url_prefix="/facts")

@bp.route('/new', methods=('GET', 'POST'))
def new_fact(): 
    if request.method == 'POST':
        name = request.form.get('name')
        pet_fact = request.form.get('pet_fact')
        
        print("Name:", name)
        print("Pet Fact:", pet_fact)
        return 'Form submitted successfully'
    else:
        return render_template('fact_pet.html')