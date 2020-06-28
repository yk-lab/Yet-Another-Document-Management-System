<template>
  <div>
    <a-form-model-item
      ref="password"
      label="パスワード"
      prop="password"
      @submit="(e) => $emit('submit', e)"
    >
      <a-input-password
        :value="value"
        placeholder="パスワードを入力してください"
        @change="(e) => $emit('input', e.target.value)"
      >
        <a-icon slot="prefix" type="lock" />
      </a-input-password>
    </a-form-model-item>
  </div>
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
