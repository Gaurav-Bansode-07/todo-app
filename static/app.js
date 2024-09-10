document.addEventListener('DOMContentLoaded', function () {
    fetchTodos();
    
    document.getElementById('todo-form').addEventListener('submit', function (event) {
        event.preventDefault();
        addTodo();
    });
});

function fetchTodos() {
    fetch('/todos')
        .then(response => response.json())
        .then(todos => {
            const todoList = document.getElementById('todo-list');
            todoList.innerHTML = '';
            todos.forEach(todo => {
                const todoItem = document.createElement('div');
                todoItem.classList.add('todo-item');
                if (todo.completed) {
                    todoItem.classList.add('complete');
                }
                todoItem.innerHTML = `
                    <h3>${todo.title}</h3>
                    <p>${todo.description}</p>
                    <button onclick="toggleComplete(${todo.id}, ${todo.completed})">${todo.completed ? 'Mark as Incomplete' : 'Mark as Complete'}</button>
                    <button onclick="deleteTodo(${todo.id})">Delete</button>
                `;
                document.getElementById('todo-list').appendChild(todoItem);
            });
        });
}

function addTodo() {
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;

    fetch('/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title,
            description: description
        })
    })
    .then(response => response.json())
    .then(todo => {
        fetchTodos();
        document.getElementById('todo-form').reset();
    });
}

function toggleComplete(id, currentStatus) {
    fetch(`/todos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            completed: !currentStatus // Toggle status
        })
    })
    .then(() => fetchTodos());
}

function deleteTodo(id) {
    fetch(`/todos/${id}`, {
        method: 'DELETE'
    })
    .then(() => fetchTodos());
}
