import client from "lib/api/client"

// test
export const execHello = () => {
  return client.get("/hello")
}
