/* eslint-disable */
export type JSONWebToken = {
  username: string
  password: string
}

export type RefreshJSONWebToken = {
  token: string
}

export type VerifyJSONWebToken = {
  token: string
}

export type Tag = {
  id?: string
  code?: string
}

export type Document = {
  id?: string
  title: string
  summary?: string
  tags: Tag[]
  filesets: string[]
  created?: string
  modified?: string
  registered_by?: string
}
