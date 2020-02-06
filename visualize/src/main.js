import Vue from 'vue'
import router from './router'
import App from './App.vue'
import { PerfectScrollbar } from 'vue2-perfect-scrollbar'

Vue.config.productionTip = false

new Vue({
  router,
  PerfectScrollbar,
  render: h => h(App),
}).$mount('#app')
