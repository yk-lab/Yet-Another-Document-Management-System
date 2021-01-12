<template>
  <div class="container">
    index page
    <nuxt-link slot="title" :to="{ name: 'documents' }">
      documents
    </nuxt-link>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({})
</script>
