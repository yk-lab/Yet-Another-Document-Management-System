<template>
  <a-form-model :model="form" :label-col="labelCol" :wrapper-col="wrapperCol">
    <a-form-model-item label="タイトル">
      <a-input
        ref="title"
        v-model="form.title"
        placeholder="タイトルを入力してください"
      ></a-input>
    </a-form-model-item>
    <a-form-model-item label="タグ">
      <a-select
        v-model="form.tags"
        mode="tags"
        style="width: 100%;"
        placeholder="タグを設定してください"
        :max-tag-text-length="256"
        :loading="tagLoading"
      >
        <a-select-option v-for="tag in tags" :key="tag.code">
          {{ tag.code }}
        </a-select-option>
      </a-select>
    </a-form-model-item>
    <a-form-model-item label="概要">
      <SummaryEditor v-model="form.summary" />
    </a-form-model-item>
    <a-form-model-item label="添付ファイル">
      <InputFile
        :action="fileUploadUrl"
        :before-upload="beforeUpload"
        :data="fileUploadData"
        :multiple="true"
        method="PUT"
        @change="handleFileChange"
      />
    </a-form-model-item>
    <a-form-model-item :wrapper-col="{ span: 14, offset: 4 }">
      <a-button type="primary" @click="onSubmit">保存</a-button>
      <a-button style="margin-left: 10px;">キャンセル</a-button>
    </a-form-model-item>
  </a-form-model>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from '@vue/composition-api'
// import { UploadChangeParam } from 'ant-design-vue/lib/upload'
import { UploadFile } from 'ant-design-vue/types/upload'
import _ from 'lodash'
import { Tag } from '../api/@types'

type UploadChangeParam = {
  file: UploadFile
  fileList: UploadFile[]
  event: ProgressEvent | undefined
}

// TODO: 将来的にちゃんと API 側で型定義する
type CreateForm = {
  title: string
  tags: string[] | Tag[]
  summary: string
  filesets: string[]
}

export default defineComponent({
  setup(_props, context) {
    const labelCol = ref({ span: 4 })
    const wrapperCol = ref({ span: 14 })

    const tagLoading = ref(false)
    const tags = ref<Tag[]>([])

    const fileUploadUrl = ref('')
    const fileUploadData = ref({})

    const formInit = ref<CreateForm>({
      title: '',
      tags: [],
      summary: '',
      filesets: [],
    })

    const form = ref<CreateForm>({
      title: '',
      tags: [],
      summary: '',
      filesets: [],
    })

    const getTags = async (): Promise<void> => {
      tagLoading.value = true
      tags.value = await context.root.$api.tags.$get()
      tagLoading.value = false
    }

    const beforeUpload = async (file: UploadFile, _filelist: UploadFile[]) => {
      try {
        const body = await context.root.$api.upload.$post({
          body: {
            file_name: file.name,
          },
        })
        // @ts-ignore
        fileUploadUrl.value = body?.action
        // @ts-ignore
        fileUploadData.value = body?.fields
        // @ts-ignore
        file.url = body?.url
      } catch (e) {
        if (e instanceof Error) {
          context.root.$notification.error({
            message: e.name,
            description: e.message,
          })
        }
        throw e
      }
    }

    const onSubmit = () => {
      const submit = _.cloneDeep(form)
      // @ts-ignore
      submit.value.tags = submit.value.tags.map(
        // @ts-ignore
        (value): Tag => {
          if (typeof value === 'string') {
            // @ts-ignore
            return { code: value }
          }
          return value
        }
      )
      try {
        context.root.$api.documents.$post({
          // @ts-ignore
          body: submit.value,
        })
      } catch (e) {
        if (e instanceof Error) {
          context.root.$notification.error({
            message: e.name,
            description: e.message,
          })
        }
        throw e
      }
      context.root.$message.success('保存しました！')
      form.value = formInit.value
    }

    const handleFileChange = (info: UploadChangeParam) => {
      window.console.log(info)
      if (info.file.status === 'done') {
        if (info.file.url) {
          form.value.filesets = [...form.value.filesets, info.file.url]
        }
        context.root.$message.success(
          `${info.file.name} file uploaded successfully`
        )
      } else if (info.file.status === 'error') {
        context.root.$message.error(`${info.file.name} file upload failed.`)
      }
    }

    onMounted(() => {
      // TODO Tag のサーバサイド検索
      getTags()
    })

    return {
      labelCol,
      wrapperCol,
      tagLoading,
      tags,
      fileUploadUrl,
      fileUploadData,
      form,
      beforeUpload,
      onSubmit,
      handleFileChange,
    }
  },
})
</script>
