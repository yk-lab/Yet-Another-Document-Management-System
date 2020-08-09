<template>
  <LoginForm
    v-bind.sync="loginData"
    :loading="isLoading"
    @onSubmit="loginWithAuthModule"
  />
</template>

<script lang="ts">
import { defineComponent, ref } from '@vue/composition-api'

export type LoginData = {
  username: string
  password: string
}

export default defineComponent({
  setup(_props, context) {
    const loginData = ref<LoginData>({
      username: '',
      password: '',
    })
    const isLoading = ref(false)

    const loginWithAuthModule = async () => {
      try {
        await context.root.$auth.loginWith('local', { data: loginData.value })
        context.root.$message.success('Logged In!')
        context.root.$router.replace({ path: '/' })
      } catch (e) {
        window.console.log(e)
        context.root.$notification.error({
          message: e.name,
          description: e.message,
        })
      }
    }

    return {
      loginData,
      isLoading,
      loginWithAuthModule,
    }
  },
})
</script>
