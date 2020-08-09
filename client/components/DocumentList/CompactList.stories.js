import { storiesOf } from '@storybook/vue'
import { array } from '@storybook/addon-knobs/vue'
import CompactList from './CompactList.vue'

storiesOf('Atoms/DocumentList', module).add(
  'CompactList',
  () => ({
    components: { CompactList },
    template: `<CompactList :documents='documents'>`,
    props: {
      documents: {
        type: Array,
        default: array('document', [
          {
            title: 'title here1',
            summary: 'summary here',
            tags: [],
            filesets: [],
          },
          {
            title: 'title here2',
            summary: 'summary here',
            tags: [],
            filesets: [],
          },
          {
            title: 'title here3',
            summary: 'summary here',
            tags: [],
            filesets: [],
          },
        ]),
      },
    },
    description: {
      CompactList: {
        props: {
          documents: '書類のリスト',
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
  }
)
