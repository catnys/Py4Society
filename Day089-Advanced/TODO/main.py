from flask import Flask, request, jsonify
from models import db, Board, Task
from board import Task,Board

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
db.init_app(app)

@app.route('/boards', methods=['POST'])
def create_board():
    data = request.get_json()
    new_board = Board(name=data['name'])
    db.session.add(new_board)
    db.session.commit()
    return jsonify({'message': 'New board created'}), 201

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(content=data['content'], board_id=data['board_id'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'New task added'}), 201

# Add routes for updating tasks and deleting boards/tasks here

if __name__ == '__main__':
    app.run(debug=True)
