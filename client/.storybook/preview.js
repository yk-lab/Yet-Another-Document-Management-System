import { configure, addDecorator } from '@storybook/vue'
import { withKnobs } from '@storybook/addon-knobs/vue'
import { withInfo } from 'storybook-addon-vue-info'

import Vue from 'vue'
import Vuex from 'vuex'
import Antd from 'ant-design-vue/lib'
import 'ant-design-vue/dist/antd.less'


Vue.use(Vuex)
Vue.use(Antd)

// automatically import all files ending in *.stories.js
const req = require.context('../components', true, /.stories.js$/)
function loadStories() {
  req.keys().forEach(filename => req(filename))
}

configure(loadStories, module)
addDecorator(withKnobs)
addDecorator(withInfo)