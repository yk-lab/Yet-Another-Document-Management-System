<template>
  <div>
    <login-modal-base
      v-bind.sync="loginData"
      :visible="showLoginModal"
      :confirm-loading="loginConfirmLoading"
      @ok="loginWithAuthModule"
      @cancel="cancelLogin"
    ></login-modal-base>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from '@vue/composition-api'

export type LoginData = {
  username: string
  password: string
}

export default defineComponent({
  setup(_props, context) {
    const showLoginModal = ref(false)
    const loginConfirmLoading = ref(false)
    const loginData = ref<LoginData>({
      username: '',
      password: '',
    })

    const loginWithAuthModule = async () => {
      loginConfirmLoading.value = true
      await context.root.$auth.loginWith('local', { data: loginData.value })
      loginConfirmLoading.value = false
      showLoginModal.value = false
      context.root.$message.success('Logged In!')
    }

    const cancelLogin = () => {
      context.root.$auth.logout()
      context.root.$router.replace({ path: '/' })
    }

    setInterval(async () => {
      if (!showLoginModal.value && context.root.$auth.loggedIn) {
        const jwtToken = context.root.$auth.getToken('local')?.split(' ')?.[1]
        try {
          await context.root.$api.api_token.verify.$post({
            body: { token: jwtToken },
          })
        } catch (error) {
          if (error.response) {
            if (
              error.response.data?.['non_field_errors']?.includes(
                'Signature has expired.'
              )
            ) {
              showLoginModal.value = true
            }
          }
        }
      }
    }, 10000)
    onMounted(() => {})

    return {
      loginData,
      showLoginModal,
      loginWithAuthModule,
      loginConfirmLoading,
      cancelLogin,
    }
  },
})
</script>
