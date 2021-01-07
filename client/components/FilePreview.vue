<template>
  <a-card hoverable style="width: 80%;">
    <object slot="cover" :data="src" height="500px"></object>
    <a-card-meta :title="name">
      <a-icon v-if="icon" slot="avatar" :type="icon" />
      <template slot="description"></template>
    </a-card-meta>
  </a-card>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'
// import pdf from 'vue-pdf'

type Props = {
  src: string
  name: String
}

export default defineComponent({
  props: {
    src: {
      type: String,
      required: true,
    },
    name: {
      type: String,
    },
  },
  // components: {
  //   pdf,
  // },
  setup(props: Props, _context) {
    const _name = props.name.toLowerCase()
    let icon = 'file'
    if (_name) {
      if (_name.endsWith('.pdf')) {
        icon = 'file-pdf'
      } else if (_name.endsWith('.jpg') || _name.endsWith('.jpeg')) {
        icon = 'file-jpg'
      } else if (_name.endsWith('.png') || _name.endsWith('.git')) {
        icon = 'file-image'
      } else if (_name.endsWith('.zip')) {
        icon = 'file-zip'
      } else if (_name.endsWith('.txt')) {
        icon = 'file-text'
      } else if (
        _name.endsWith('.doc') ||
        _name.endsWith('.docx') ||
        _name.endsWith('.odt')
      ) {
        icon = 'file-word'
      } else {
        icon = 'file-unknown'
      }
    }

    return {
      icon,
    }
  },
})
</script>
