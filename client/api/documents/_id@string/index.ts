/* eslint-disable */
import * as Types from '../../@types'

export type Methods = {
  get: {
    status: 200
    resBody: Types.Document
  }

  put: {
    status: 200
    resBody: Types.Document
    reqBody: Types.Document
  }

  patch: {
    status: 200
    resBody: Types.Document
    reqBody: Types.Document
  }

  delete: {
    status: 204
  }
}
