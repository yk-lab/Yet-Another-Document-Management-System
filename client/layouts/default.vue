<template>
  <div>
    <a-config-provider :locale="locale">
      <Nuxt />
    </a-config-provider>
    <login-modal />
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'
import { Locale } from 'ant-design-vue/types/locale-provider'
import jaJP from 'ant-design-vue/lib/locale-provider/ja_JP'
import moment from 'moment'
import 'moment/locale/ja'
moment.locale('ja')

export default defineComponent({
  setup(_props, _context) {
    const locale: Locale = jaJP

    return {
      locale,
    }
  },
})
</script>
