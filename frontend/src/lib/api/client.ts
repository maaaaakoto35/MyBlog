import applyCaseMiddleware from 'axios-case-converter'
import axios from 'axios'

// applyCaseMiddleware:
// axiosで受け取ったレスポンスの値をスネークケース->キャメルケースに変換
// リクエストの値をキャメルケース　->スネークケースに変換してくれるライブラリ

// ヘッダーはキャメルケースで良い
const options = {
  ignoreHeaders: true
}

const client = applyCaseMiddleware(axios.create({
  baseURL: "http://localhost:9000/api/v1"
}), options)

export default client
