from flask import Flask, render_template, redirect, flash, session, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy 
from models import db, connect_db, Cupcake
from tools import Tools
from forms import AddCupcakeForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SECRET KEY'] = "There's_no_spoon"
app.config['SECRET_KEY'] = "There's_no_spoon"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/api/cupcakes')
def send_all_cupcakes():
    """Serializes each cupcake instance and send it as JSON"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def send_single_cupcake(id):
    """Serialized a single cupcake instance and sends it as JSON"""
    single_cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=single_cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def new_cupcake():
    """Creates a new instance of Cupcake and adds it to the database"""
    new_cupcake = Tools.new_cupcake(request.json)

    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def patch_cupcake(id):
    """Updates a cupcake instance"""
    updated_cupcake = Tools.update_cupcake(id, request.json)

    return jsonify(cupcake=updated_cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Deletes the cupcake instance"""
    
    return Tools.delete_cupcake(id)

@app.route('/')
def homepage():
    """Render a homepage with a list of cupcakes and a form to add more cupcakes"""
    form = AddCupcakeForm()

    return render_template('home.html', form=form)


    






    






