<template>
  <DocumentDetail :document="document"></DocumentDetail>
</template>

<script lang="ts">
import { defineComponent, ref, watchEffect } from '@vue/composition-api'
import { Document } from '~/api/@types'

export default defineComponent({
  validate({ params }) {
    // UUIDでなければならない
    return /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/.test(
      params.id
    )
  },
  setup(_props, context) {
    const document = ref<Document | undefined>(undefined)
    watchEffect(async () => {
      document.value = await context.root.$api.documents
        ._id(context.root.$route.params.id)
        .$get()
    })

    return {
      document,
    }
  },
})
</script>
