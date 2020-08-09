<template>
  <a-modal
    title="ログイン"
    :visible="visible"
    :confirm-loading="confirmLoading"
    v-on="$listeners"
  >
    <a-form-model :layout="layout" v-bind="formItemLayout">
      <login-form-user-name
        :value="username"
        @input="(v) => $emit('update:username', v)"
      />
      <login-form-password
        :value="password"
        @input="(v) => $emit('update:password', v)"
      />
    </a-form-model>
  </a-modal>
</template>

<script lang="ts">
import { defineComponent, computed } from '@vue/composition-api'

type Props = {
  layout: string
  username: string
  password: string
  visible: boolean
  confirmLoading: boolean
}

export default defineComponent({
  props: {
    visible: {
      type: Boolean,
      default: true,
    },
    confirmLoading: {
      type: Boolean,
      default: false,
    },
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
  },
  setup(props: Props, _context) {
    const layout = props.layout

    const formItemLayout = computed(() => {
      return layout === 'horizontal'
        ? {
            labelCol: { span: 4 },
            wrapperCol: { span: 14 },
          }
        : {}
    })

    return {
      formItemLayout,
    }
  },
})
</script>
