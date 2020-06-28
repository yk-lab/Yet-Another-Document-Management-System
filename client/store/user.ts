import { Module, VuexModule, Mutation } from 'vuex-module-decorators'

export interface IUserState {
  token: string | null
}

@Module({
  name: 'user',
  stateFactory: true,
  namespaced: true,
})
export default class UserModule extends VuexModule implements IUserState {
  // state
  token: string | null = null

  // mutation
  @Mutation
  setToken(token: string) {
    this.token = token
  }
}
