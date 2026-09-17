import { defineStore } from 'pinia'
import client from '../api/client'

export const use_auth_store = defineStore('auth', {
  state: () => ({ user: null }),
  getters: { is_authenticated: () => Boolean(localStorage.getItem('access_token')) },
  actions: {
    async login(credentials) {
      const { data } = await client.post('/auth/login', credentials)
      localStorage.setItem('access_token', data.access_token)
      await this.fetch_current_user()
    },
    async fetch_current_user() {
      const { data } = await client.get('/auth/me')
      this.user = data
      return data
    },
    logout() {
      localStorage.removeItem('access_token')
      this.user = null
    },
  },
})
