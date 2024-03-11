import { createRouter, createWebHistory } from 'vue-router'
import Promoo from '@/views/Promoo.vue'
import Quartos from '@/views/Quartos.vue'
import RemovePoppup from '@/components/RemovePoppup.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/rooms-page',
      name: 'room',
      component: Quartos
    },
    {
      path: '/promotion-page/:id',
      name: 'promotion',
      component: Promoo
    },
    {
      path: '/remove-page/:id',
      name:'remove',
      component: RemovePoppup
    }
  ]
})

export default router
