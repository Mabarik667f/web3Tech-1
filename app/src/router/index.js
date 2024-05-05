import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

import HomeView from '../views/HomeView.vue'
import ClientRegisterView from "@/views/ClientRegisterView.vue";
import MakerRegisterView from "@/views/MakerRegisterView.vue";
import DistributorRegisterView from "@/views/DistributorRegisterView.vue";
import ProfileView from "@/views/ProfileView.vue";
import OperatorRegisterView from "@/views/OperatorRegisterView.vue";
import CreateOrderView from "@/views/CreateOrderView.vue";
import CreateProductView from "@/views/CreateProductView.vue";
import LoginView from "@/views/LoginView.vue";
import ProductCardsView from "@/views/ProductCardsView.vue";

const authGuard = (to, from, next) => {
  if (!store.state.auth.isAuth) {
    next('/')
  } else {
    next()
  }
}
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/operator',
    name: 'operator',
    component: OperatorRegisterView
  },
  {
    path: '/client',
    name: 'client',
    component: ClientRegisterView
  },
  {
    path: '/maker',
    name: 'maker',
    component: MakerRegisterView
  },
  {
    path: '/distributor',
    name: 'distributor',
    component: DistributorRegisterView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    beforeEnter: authGuard
  },
  {
    path: '/createProduct',
    name: 'createProduct',
    component: CreateProductView,
  },
  {
    path: '/createOrder',
    name: 'createOrder',
    component: CreateOrderView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/products',
    name: 'products',
    component: ProductCardsView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  store.dispatch('getStorage').then(() => {
    next();
  })
})

export default router
