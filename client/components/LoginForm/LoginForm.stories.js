import { storiesOf } from '@storybook/vue'
import { object } from '@storybook/addon-knobs/vue'
import LoginForm from './LoginForm'

storiesOf('Atoms/login forms', module).add(
  'LoginForm',
  () => ({
    components: { LoginForm },
    template: `<LoginForm v-bind.sync='formData'/>`,
    props: {
      formData: {
        type: Object,
        default: object('Model', {
          username: '',
          password: '',
        }),
      },
    },
    description: {
      LoginForm: {
        props: {},
      },
    },
  }),
  {
    info: true,
    notes: `
        # Input File

        ## Props
        * action
          * string
            * 送信先
        * multiple
          * boolean
            * 複数ファイル可否
        `,
  })