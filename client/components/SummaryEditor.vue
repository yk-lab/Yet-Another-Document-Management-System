<template>
  <a-row :gutter="16">
    <a-col :span="12">
      <a-textarea
        :placeholder="placeholder"
        :rows="rows"
        :value="value"
        @input="update"
      />
    </a-col>
    <a-col :span="12">
      <div class="preview" v-html="compiledMarkdown"></div>
    </a-col>
  </a-row>
</template>

<script lang="ts">
import Vue from 'vue'
// import _ from 'lodash'
import marked from 'marked'

export default Vue.extend({
  props: {
    placeholder: {
      type: String,
      default: '概要を入力してください',
    },
    rows: {
      type: Number,
      default: 4,
    },
    value: {
      type: String,
      default: '',
    },
  },
  computed: {
    compiledMarkdown() {
      return marked(this.value)
    },
  },
  methods: {
    update(e: InputEvent) {
      if (
        e.target instanceof HTMLInputElement ||
        e.target instanceof HTMLTextAreaElement
      ) {
        this.$emit('input', e.target.value)
      }
      // return _.debounce((e) => {
      //   this.$emit('input', e.target.value)
      // }, 3)
    },
  },
})
</script>
