import React from "react";
import { TodoItem } from "./TodoItem";
import { Todo } from "../types/Todo";

type Props = {
    todos: Todo[]
    setTodos: React.Dispatch<React.SetStateAction<Todo[]>>
}

export const TodoList: React.FC<Props> = ({ todos, setTodos }) => {
    const handleDone = (todo: Todo) => {
        setTodos(prev => prev.map(t =>
            t.id === todo.id
                ? { ...todo, done: !todo.done }
                : t
        ))
    }

    const handleDelete = (todo: Todo) => {
        setTodos(prev => prev.filter(t =>
            t.id !== todo.id
        ))
    }

    return (
        <div className="inner">
            {
                todos.length <= 0 ? '登録されたTODOはありません' :
                <ul className="todo-list">
                    {
                        todos.map( todo => (
                            <TodoItem
                                key={todo.id}
                                todo={todo}
                                handleDelete={handleDelete}
                                handleDone={handleDone}
                            />
                        ))
                    }
                </ul>
            }
        </div>
    )
}
