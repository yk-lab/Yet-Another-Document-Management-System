<template>
  <a-form-model-item :wrapper-col="wrapperCol">
    <a-button
      type="primary"
      :disabled="disabled"
      :loading="loading"
      @click="(e) => $emit('onSubmit', e)"
    >
      ログイン
    </a-button>
  </a-form-model-item>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    wrapperCol: {
      type: Object,
      default: () => {
        return { span: 14, offset: 4 }
      },
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
})
</script>
