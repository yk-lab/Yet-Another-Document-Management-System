<template>
  <a-list size="large" item-layout="horizontal" :data-source="documents">
    <a-list-item slot="renderItem" slot-scope="item">
      <a-list-item-meta :description="item.summary">
        <nuxt-link
          slot="title"
          :to="{ name: 'documents-id', params: { id: item.id } }"
        >
          {{ item.title }}
        </nuxt-link>
      </a-list-item-meta>
    </a-list-item>
  </a-list>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue'
import { Document } from '../../api/@types'

export default Vue.extend({
  props: {
    documents: {
      type: Array as PropType<Document[]>,
      default: () => [],
    },
  },
  computed: {},
})
</script>
