import React, { useEffect, useState } from "react"

import { execHello } from "lib/api/hello"

const App: React.FC = () => {
  const [message, setMessage] = useState<string>("")

  const handleExecHello = async () => {
    const res = await execHello()

    if (res.status === 200) {
      setMessage(res.data.message)
    }
  }

  useEffect(() => {
    handleExecHello()
  }, [])

  return (
    <h1>{message}</h1>
  )
}

export default App
