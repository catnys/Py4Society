from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
