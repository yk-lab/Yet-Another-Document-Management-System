<template>
  <a-spin :spinning="initLoading" tip="Loading...">
    <div class="spin-content">
      <CompactList :documents="documents"></CompactList>
    </div>
  </a-spin>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from '@vue/composition-api'
import { Document } from '~/../../api/@types'

export default defineComponent({
  setup(_props, context) {
    const documents = ref<Document[]>([])
    const initLoading = ref(false)

    onMounted(async () => {
      initLoading.value = true
      documents.value = await context.root.$api.documents.$get()
      initLoading.value = false
    })

    return {
      documents,
      initLoading,
    }
  },
})
</script>
