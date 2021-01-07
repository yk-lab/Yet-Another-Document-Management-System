<template>
  <a-form-model-item ref="username" label="ユーザ名" prop="username">
    <a-input
      :value="value"
      placeholder="ユーザ名を入力してください"
      @change="(e) => $emit('input', e.target.value)"
    >
      <a-icon slot="prefix" type="user" />
    </a-input>
  </a-form-model-item>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: {
    value: {
      type: String,
      required: true,
    },
  },
})
</script>
