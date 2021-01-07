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
  id: string
  code: string
}

export type File = {
  id: string
  file: string
  filename: string
  fileset: string
  memo: string
  is_removed: boolean
  created: string
  modified: string
}

export type Fileset = {
  id?: string
  name: string
  files: File[]
}

export type Document = {
  id?: string
  title: string
  summary?: string
  tags: Tag[]
  filesets: Fileset[]
  created?: string
  modified?: string
  registered_by?: string
}

export type Upload = {
  file_name: string
  action?: string

  fields?: {
    [key: string]: string
  }
}
