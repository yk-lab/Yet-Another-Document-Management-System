import { storiesOf } from '@storybook/vue'
import { text, boolean } from '@storybook/addon-knobs/vue'
import InputFile from './InputFile.vue'

storiesOf('Atoms/forms', module).add(
  'InputForm',
  () => ({
    components: { InputFile },
    template: `<InputFile :action='action' :multiple='multiple' :list-type='listType'>`,
    props: {
      action: {
        type: String,
        default: text('action', ''),
      },
      multiple: {
        type: Boolean,
        default: boolean('multiple', false),
      },
      listType: {
        type: String,
        default: text('listType', 'text'),
      },
    },
    description: {
      InputFile: {
        props: {
          action: '送信先設定',
          multiple: '複数ファイル可否',
          listType: 'ファイルリスト (text, picture, picture-card)',
        },
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