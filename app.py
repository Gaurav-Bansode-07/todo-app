from flask import Flask, request, jsonify, render_template
from models import db, Todo
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create tables when the app starts
with app.app_context():
    db.create_all()

# Route to retrieve all to-do items
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

# Route to add a new to-do item
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()

    # Ensure title and description are provided
    if 'title' not in data or 'description' not in data:
        return jsonify({'error': 'Title and description are required.'}), 400
    
    try:
        new_todo = Todo(title=data['title'], description=data['description'], completed=False)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(new_todo.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create the to-do item.'}), 500

# Route to update a to-do item
@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    todo = Todo.query.get_or_404(id)

    # Update fields if provided
    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)

    db.session.commit()
    return jsonify(todo.to_dict())

# Route to delete a to-do item
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'To-do item deleted successfully.'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
