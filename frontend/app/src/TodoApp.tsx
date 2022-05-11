import React, { useState } from "react";
import { TodoInput } from "./components/TodoInput";
import { TodoList } from "./components/TodoList";
import './TodoApp.css';
import { Todo } from "./types/Todo";

const initialState: Todo[] = [
    {
        id: 2,
        text: '散歩',
        done: false
    },
    {
        id: 1,
        text: 'サッカー',
        done: false
    }
]

function TodoApp() {
    const [todos, setTodos] = useState(initialState);

    return (
        <div>
            <TodoInput setTodos={setTodos} todos={todos} />
            <TodoList setTodos={setTodos} todos={todos} />
        </div>
    )
}

export default TodoApp;
