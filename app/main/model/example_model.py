from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ExampleModel(db.Model):
    __tablename__ = 'examples'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))