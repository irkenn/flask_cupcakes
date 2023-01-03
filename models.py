from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import Computed


db = SQLAlchemy()

def connect_db(app):
	db.app = app
	db.init_app(app)

class Cupcake(db.Model):
    """This is the class model for cupcakes"""

    __tablename__ = 'cupcakes'

    def __repr__(self):
        p = self
        return f"Cupcake id={p.id} flavor={p.flavor}"

    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text,  nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default='https://tinyurl.com/demo-cupcake')
    
    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }


