<template>
  <a-form-model :layout="layout" v-bind="formItemLayout">
    <user-name :value="username" @input="(v) => $emit('update:username', v)" />
    <password :value="password" @input="(v) => $emit('update:password', v)" />
    <submit-button
      :disabled="username === '' || password === ''"
      :loading="loading"
      v-bind="buttonItemLayout"
      @onSubmit="(e) => $emit('onSubmit', e)"
    />
  </a-form-model>
</template>

<script lang="ts">
import Vue from 'vue'
import LoginFormUserName from './LoginFormUserName.vue'
import LoginFormPassword from './LoginFormPassword.vue'
import LoginFormSubmitButton from './LoginFormSubmitButton.vue'

export default Vue.extend({
  components: {
    userName: LoginFormUserName,
    password: LoginFormPassword,
    submitButton: LoginFormSubmitButton,
  },
  props: {
    layout: {
      type: String,
      default: 'horizontal',
    },
    username: {
      type: String,
      required: true,
    },
    password: {
      type: String,
      required: true,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    formItemLayout() {
      return this.layout === 'horizontal'
        ? {
            labelCol: { span: 4 },
            wrapperCol: { span: 14 },
          }
        : {}
    },
    buttonItemLayout() {
      return this.layout === 'horizontal'
        ? {
            wrapperCol: { span: 14, offset: 4 },
          }
        : {}
    },
  },
})
</script>
