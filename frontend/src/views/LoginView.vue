<script setup>
import { ref } from 'vue'
import client from '../api/client'

const checking = ref(false)
const service_status = ref('尚未检测')

async function check_api() {
  checking.value = true
  try {
    const { data } = await client.get('/health')
    service_status.value = data.status === 'ok' ? '后端服务正常' : '后端返回异常'
  } catch {
    service_status.value = '无法连接后端'
  } finally {
    checking.value = false
  }
}
</script>

<template>
  <main class="login-page">
    <el-card class="login-card" shadow="never">
      <h1>AI 合同风险工作台</h1>
      <p>阶段一 MVP：合同、风险、任务与处理记录。</p>
      <el-button type="primary" :loading="checking" @click="check_api">检测后端连接</el-button>
      <p class="status">{{ service_status }}</p>
    </el-card>
  </main>
</template>
