import Vue from 'vue'
import { Configuration } from '@nuxt/types'
import { Auth } from 'nuxtjs__auth'

const nuxtConfig: Configuration = {
  /*
   ** Nuxt rendering mode
   ** See https://nuxtjs.org/api/configuration-mode
   */
  mode: 'spa',
  /*
   ** Nuxt target
   ** See https://nuxtjs.org/api/configuration-target
   */
  target: 'static',
  /*
   ** Headers of the page
   ** See https://nuxtjs.org/api/configuration-head
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || '',
      },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },
  /*
   ** Global CSS
   */
  css: ['ant-design-vue/dist/antd.css'],
  /*
   ** Plugins to load before mounting the App
   ** https://nuxtjs.org/guide/plugins
   */
  plugins: [
    '@/plugins/antd-ui',
    '@/plugins/api',
    '@/plugins/axios.accessor',
    '@/plugins/composition-api',
  ],
  /*
   ** Auto import components
   ** See https://nuxtjs.org/api/configuration-components
   */
  components: true,
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    '@nuxt/typescript-build',
    '@nuxtjs/eslint-module',
    // Doc: https://github.com/nuxt-community/stylelint-module
    '@nuxtjs/stylelint-module',
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxtjs/auth',
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: 'http://127.0.0.1:8000', // aspidaにもbaseURLが反映されます
  },
  auth: {
    redirect: {
      login: '/login',
      logout: '/login',
      callback: false,
      home: '/',
    },
    strategies: {
      local: {
        endpoints: {
          login: {
            url: '/api-token/auth',
            method: 'post',
            propertyName: 'token',
          },
          logout: false,
          user: false,
        },
        tokenType: 'JWT',
      },
    },
    rewriteRedirects: true,
    watchLoggedIn: false,
  },
  /*
   ** Build configuration
   ** See https://nuxtjs.org/api/configuration-build/
   */
  build: {},
  router: {
    middleware: ['auth'],
  },
}

declare module 'vue/types/vue' {
  interface Vue {
    $auth: Auth
  }
}

module.exports = nuxtConfig
