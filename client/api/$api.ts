/* eslint-disable */
import { AspidaClient, BasicHeaders } from 'aspida'
import { Methods as Methods0 } from './api-token/auth'
import { Methods as Methods1 } from './api-token/refresh'
import { Methods as Methods2 } from './api-token/verify'
import { Methods as Methods3 } from './documents'
import { Methods as Methods4 } from './documents/_id@string'
import { Methods as Methods5 } from './tags'
import { Methods as Methods6 } from './tags/_id@string'
import { Methods as Methods7 } from './upload'
import { Methods as Methods8 } from './upload{format}'

const GET = 'GET'
const POST = 'POST'
const PUT = 'PUT'
const DELETE = 'DELETE'
const PATCH = 'PATCH'
const PATH0 = '/api-token/auth'
const PATH1 = '/api-token/refresh'
const PATH2 = '/api-token/verify'
const PATH3 = '/documents/'
const PATH4 = '/tags/'
const PATH5 = '/upload/'
const PATH6 = '/upload{format}'
const api = <T>({ baseURL, fetch }: AspidaClient<T>) => {
  const prefix = (baseURL === undefined ? 'http://localhost:8000/' : baseURL).replace(/\/$/, '')

  return {
    api_token: {
      auth: {
        post: (option: { body: Methods0['post']['reqBody'], config?: T }) =>
          fetch<Methods0['post']['resBody'], BasicHeaders, Methods0['post']['status']>(prefix, PATH0, POST, option).json(),
        $post: (option: { body: Methods0['post']['reqBody'], config?: T }) =>
          fetch<Methods0['post']['resBody'], BasicHeaders, Methods0['post']['status']>(prefix, PATH0, POST, option).json().then(r => r.body)
      },
      refresh: {
        post: (option: { body: Methods1['post']['reqBody'], config?: T }) =>
          fetch<Methods1['post']['resBody'], BasicHeaders, Methods1['post']['status']>(prefix, PATH1, POST, option).json(),
        $post: (option: { body: Methods1['post']['reqBody'], config?: T }) =>
          fetch<Methods1['post']['resBody'], BasicHeaders, Methods1['post']['status']>(prefix, PATH1, POST, option).json().then(r => r.body)
      },
      verify: {
        post: (option: { body: Methods2['post']['reqBody'], config?: T }) =>
          fetch<Methods2['post']['resBody'], BasicHeaders, Methods2['post']['status']>(prefix, PATH2, POST, option).json(),
        $post: (option: { body: Methods2['post']['reqBody'], config?: T }) =>
          fetch<Methods2['post']['resBody'], BasicHeaders, Methods2['post']['status']>(prefix, PATH2, POST, option).json().then(r => r.body)
      }
    },
    documents: {
      _id: (val0: string) => {
        const prefix0 = `${PATH3}${val0}`

        return {
          get: (option?: { config?: T }) =>
            fetch<Methods4['get']['resBody'], BasicHeaders, Methods4['get']['status']>(prefix, prefix0, GET, option).json(),
          $get: (option?: { config?: T }) =>
            fetch<Methods4['get']['resBody'], BasicHeaders, Methods4['get']['status']>(prefix, prefix0, GET, option).json().then(r => r.body),
          put: (option: { body: Methods4['put']['reqBody'], config?: T }) =>
            fetch<Methods4['put']['resBody'], BasicHeaders, Methods4['put']['status']>(prefix, prefix0, PUT, option).json(),
          $put: (option: { body: Methods4['put']['reqBody'], config?: T }) =>
            fetch<Methods4['put']['resBody'], BasicHeaders, Methods4['put']['status']>(prefix, prefix0, PUT, option).json().then(r => r.body),
          patch: (option: { body: Methods4['patch']['reqBody'], config?: T }) =>
            fetch<Methods4['patch']['resBody'], BasicHeaders, Methods4['patch']['status']>(prefix, prefix0, PATCH, option).json(),
          $patch: (option: { body: Methods4['patch']['reqBody'], config?: T }) =>
            fetch<Methods4['patch']['resBody'], BasicHeaders, Methods4['patch']['status']>(prefix, prefix0, PATCH, option).json().then(r => r.body),
          delete: (option?: { config?: T }) =>
            fetch<void, BasicHeaders, Methods4['delete']['status']>(prefix, prefix0, DELETE, option).send(),
          $delete: (option?: { config?: T }) =>
            fetch<void, BasicHeaders, Methods4['delete']['status']>(prefix, prefix0, DELETE, option).send().then(r => r.body)
        }
      },
      get: (option?: { config?: T }) =>
        fetch<Methods3['get']['resBody'], BasicHeaders, Methods3['get']['status']>(prefix, PATH3, GET, option).json(),
      $get: (option?: { config?: T }) =>
        fetch<Methods3['get']['resBody'], BasicHeaders, Methods3['get']['status']>(prefix, PATH3, GET, option).json().then(r => r.body),
      post: (option: { body: Methods3['post']['reqBody'], config?: T }) =>
        fetch<Methods3['post']['resBody'], BasicHeaders, Methods3['post']['status']>(prefix, PATH3, POST, option).json(),
      $post: (option: { body: Methods3['post']['reqBody'], config?: T }) =>
        fetch<Methods3['post']['resBody'], BasicHeaders, Methods3['post']['status']>(prefix, PATH3, POST, option).json().then(r => r.body)
    },
    tags: {
      _id: (val1: string) => {
        const prefix1 = `${PATH4}/${val1}`

        return {
          get: (option?: { config?: T }) =>
            fetch<Methods6['get']['resBody'], BasicHeaders, Methods6['get']['status']>(prefix, prefix1, GET, option).json(),
          $get: (option?: { config?: T }) =>
            fetch<Methods6['get']['resBody'], BasicHeaders, Methods6['get']['status']>(prefix, prefix1, GET, option).json().then(r => r.body)
        }
      },
      get: (option?: { config?: T }) =>
        fetch<Methods5['get']['resBody'], BasicHeaders, Methods5['get']['status']>(prefix, PATH4, GET, option).json(),
      $get: (option?: { config?: T }) =>
        fetch<Methods5['get']['resBody'], BasicHeaders, Methods5['get']['status']>(prefix, PATH4, GET, option).json().then(r => r.body)
    },
    upload: {
      post: (option?: { body: any, config?: T }) =>
        fetch<void, BasicHeaders, Methods7['post']['status']>(prefix, PATH5, POST, option).send(),
      $post: (option?: { body: any, config?: T }) =>
        fetch<void, BasicHeaders, Methods7['post']['status']>(prefix, PATH5, POST, option).send().then(r => r.body)
    },
    upload_format_: {
      post: (option?: { config?: T }) =>
        fetch<void, BasicHeaders, Methods8['post']['status']>(prefix, PATH6, POST, option).send(),
      $post: (option?: { config?: T }) =>
        fetch<void, BasicHeaders, Methods8['post']['status']>(prefix, PATH6, POST, option).send().then(r => r.body)
    }
  }
}

export type ApiInstance = ReturnType<typeof api>
export default api
