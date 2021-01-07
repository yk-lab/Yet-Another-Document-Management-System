<template>
  <div v-if="document">
    <a-page-header :title="document.title" :sub-title="document.summary" />
    <a-descriptions bordered>
      <a-descriptions-item label="Tags">
        <a-tag v-for="tag in document.tags" :key="tag.id">{{ tag.code }}</a-tag>
      </a-descriptions-item>
      <a-descriptions-item label="Created">
        {{ moment(document.created).format('LLL') }}
      </a-descriptions-item>
      <a-descriptions-item label="Modified">
        {{ moment(document.modified).format('LLL') }}
      </a-descriptions-item>
      <a-descriptions-item label="Registered_by" :span="2">
        {{ document.registered_by }}
      </a-descriptions-item>
    </a-descriptions>
    <file-preview
      v-for="item in document.filesets"
      :key="item.id"
      :name="item.name"
      :src="item.files[item.files.length - 1].file"
    >
    </file-preview>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import moment from 'moment'

export default Vue.extend({
  props: {
    document: {
      required: true,
      validator: (prop) => typeof prop === 'object' || prop === null,
    },
  },
  data(): {} {
    return {
      moment,
    }
  },
})
</script>
