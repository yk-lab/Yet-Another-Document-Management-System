<template>
  <a-upload-dragger
    name="file"
    :multiple="multiple"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <p class="ant-upload-drag-icon">
      <a-icon type="inbox" />
    </p>
    <p class="ant-upload-text">
      クリックまたはドラッグ & ドロップしてファイルをアップロード
    </p>
    <p v-if="multiple" class="ant-upload-hint">
      単一または複数のファイルをアップロードできます
    </p>
    <p v-else class="ant-upload-hint">
      ファイルを 1 つまでアップロードできます
    </p>
  </a-upload-dragger>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  props: {
    multiple: {
      type: Boolean,
      default: false,
    },
  },
})
</script>
