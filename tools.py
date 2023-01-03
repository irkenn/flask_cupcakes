from flask import Flask, session, jsonify
from models import db, connect_db, Cupcake

class Tools():
    """This will be used to keep app.py's code less cluttered"""

    @staticmethod
    def new_cupcake(JSON_data):
        """This creates a new model instance and updated it to the database, returns the created model instance"""
        image = JSON_data.get("image") or None 
        new_cupcake = Cupcake(flavor=JSON_data["flavor"], size=JSON_data["size"], rating=JSON_data["rating"], image=image)
        db.session.add(new_cupcake)
        db.session.commit()
        
        return new_cupcake

    @staticmethod
    def update_cupcake(id, JSON_data):
        """This updates the values from the class instance, updates the database and returns the updated instance"""
        cupcake = Cupcake.query.get_or_404(id)
        cupcake.flavor = JSON_data.get("flavor", cupcake.flavor)
        cupcake.size = JSON_data.get("size", cupcake.size)
        cupcake.rating = JSON_data.get("rating", cupcake.rating)
        cupcake.image = JSON_data.get("image", cupcake.image)
        db.session.commit()

        return cupcake

    @staticmethod
    def delete_cupcake(id):
        """Deletes the instance id the passed id"""
        cupcake = Cupcake.query.get_or_404(id)
        db.session.delete(cupcake)
        db.session.commit()
        
        return jsonify(message="Deleted")

