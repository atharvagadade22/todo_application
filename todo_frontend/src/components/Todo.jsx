import React, { useState, useEffect } from "react";
import axios from "axios";
import './Todo.css';  // Import the Todo.css file

const Todo = () => {
    const [todos, setTodos] = useState([]);
    const [newTodo, setNewTodo] = useState({ Title: '', Desc: '' });

    useEffect(() => {
        fetchTodos();
    }, []);

    const fetchTodos = async () => {
        const response = await axios.get('http://127.0.0.1:8000/api/todos/');
        setTodos(response.data);
    };

    const addTodo = async () => {
        await axios.post('http://127.0.0.1:8000/api/todos', newTodo);
        setNewTodo({ Title: '', Desc: '' });
        fetchTodos();
    };

    const deleteTodo = async (id) => {
        await axios.delete(`http://127.0.0.1:8000/api/todos/${id}/`);
        fetchTodos();
    };

    return (
        <div className="todo-container">
            <h1>Todo App</h1>
            
            <div className="todo-form">
                <input
                    type="text"
                    placeholder="Title"
                    value={newTodo.Title}
                    onChange={(e) => setNewTodo({ ...newTodo, Title: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="Description"
                    value={newTodo.Desc}
                    onChange={(e) => setNewTodo({ ...newTodo, Desc: e.target.value })}
                />
                <button onClick={addTodo}>Add Todo</button>
            </div>

            <ul className="todo-list">
                {todos.map((todo) => (
                    <li key={todo.id} className="todo-item">
                        <div className="todo-content">
                            <h3>{todo.Title}</h3>
                            <p>{todo.Desc}</p>
                        </div>
                        <button onClick={() => deleteTodo(todo.id)} className="delete-button">Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Todo;
