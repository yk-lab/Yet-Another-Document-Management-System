<template>
  <login-form v-bind.sync="loginData" :loading="isLoading" @onSubmit="submit" />
</template>

<script lang="ts">
import Vue from 'vue'
import LoginForm from '@/components/LoginForm/LoginForm.vue'
import { userStore } from '@/store'

export default Vue.extend({
  components: {
    loginForm: LoginForm,
  },
  data() {
    return {
      loginData: {
        username: '',
        password: '',
      },
      isLoading: false,
    }
  },
  mounted() {
    window.console.log(this)
  },
  methods: {
    submit(_: Event): void {
      // TODO: エラーハンドリング
      this.isLoading = true
      this.$api.auth
        .post({ body: this.loginData })
        .then((res: any) => {
          userStore.setToken(res.body.token)
        })
        .finally(() => {
          this.isLoading = false
        })
    },
  },
})
</script>
