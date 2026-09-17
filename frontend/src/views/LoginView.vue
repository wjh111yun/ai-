<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { use_auth_store } from '../stores/auth'

const router = useRouter()
const auth_store = use_auth_store()
const form_ref = ref()
const submitting = ref(false)
const error_message = ref('')
const form = reactive({ username: 'admin', password: 'Admin123!' })
const rules = {
  username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
}

async function submit_login() {
  const valid = await form_ref.value.validate().catch(() => false)
  if (!valid) return
  submitting.value = true
  error_message.value = ''
  try {
    await auth_store.login(form)
    await router.replace('/dashboard')
  } catch (error) {
    error_message.value = error.response?.data?.detail || '登录失败，请稍后重试'
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <main class="login-page">
    <el-card class="login-card" shadow="never">
      <h1>AI 合同风险工作台</h1>
      <p class="subtitle">合同、风险、任务与处理记录</p>
      <el-form ref="form_ref" :model="form" :rules="rules" label-position="top" @submit.prevent="submit_login">
        <el-form-item label="账号" prop="username">
          <el-input v-model="form.username" autocomplete="username" />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="form.password" type="password" show-password autocomplete="current-password" />
        </el-form-item>
        <el-alert v-if="error_message" :title="error_message" type="error" show-icon :closable="false" />
        <el-button class="login-button" native-type="submit" type="primary" :loading="submitting">登录</el-button>
      </el-form>
      <p class="hint">演示账号：admin / Admin123!</p>
    </el-card>
  </main>
</template>
