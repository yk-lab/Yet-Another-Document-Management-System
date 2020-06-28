<template>
  <input-file />
</template>

<script lang="ts">
import Vue from 'vue'
import InputFile from '@/components/FileUpload/InputFile.vue'

export default Vue.extend({
  components: {
    'input-file': InputFile,
  },
})
</script>
