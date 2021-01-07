/* eslint-disable */
import * as Types from '../@types'

export type Methods = {
  get: {
    status: 200
    resBody: Types.Document[]
  }

  post: {
    status: 201
    resBody: Types.Document
    reqBody: Types.Document
  }
}
