import React, { useState } from "react";
import { Todo } from "../types/Todo";

type Props = {
    setTodos: React.Dispatch<React.SetStateAction<Todo[]>>
    todos: Todo[]
}

export const TodoInput: React.FC<Props> = ({ setTodos, todos }) => {
    const [ inputText, setInpuText ] = useState<string>('')
    const [ count, setCount ] = useState<number>(todos.length + 1)

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setInpuText(e.target.value)
    }

    const handleSubmit = () => {
        setCount(count + 1)
        const newTodo: Todo = {
            id: count,
            text: inputText,
            done: false
        }

        setTodos([newTodo, ...todos])
        setInpuText('')
    }

    return (
        <div>
            <div className="inputForm">
                <div className="inner">
                    <input
                        type="text"
                        className="input"
                        value={inputText}
                        onChange={handleInputChange}
                    />
                    <button onClick={handleSubmit} className="btn is-primary">追加</button>
                </div>
            </div>
        </div>
    )
}
