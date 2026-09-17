<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { use_auth_store } from '../stores/auth'

const router = useRouter()
const auth_store = use_auth_store()
const loading = ref(true)

onMounted(async () => {
  try {
    await auth_store.fetch_current_user()
  } catch {
    auth_store.logout()
    router.replace('/login')
  } finally {
    loading.value = false
  }
})

function logout() {
  auth_store.logout()
  router.replace('/login')
}
</script>

<template>
  <main class="dashboard-page" v-loading="loading">
    <section v-if="!loading" class="dashboard-card">
      <div>
        <p class="eyebrow">工作台</p>
        <h1>你好，{{ auth_store.user?.display_name }}</h1>
        <p>登录与权限基础已就绪，下一步将接入合同管理。</p>
      </div>
      <el-button @click="logout">退出登录</el-button>
    </section>
  </main>
</template>
