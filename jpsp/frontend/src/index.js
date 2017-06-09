// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import index from './index.vue'
import router from './router/index.js'
import ElementUI from 'element-ui'
import Vuex from 'vuex'
import 'element-ui/lib/theme-default/index.css'
import 'bootstrap'
import axios from 'axios'
Vue.config.productionTip = false
Vue.prototype.$ajax = axios
Vue.use(ElementUI)
Vue.use(Vuex)
/* eslint-disable no-new */

const UserVuexStore = new Vuex.Store({
  state: {
    UserName: '用户名',
    UserId: '',
    Token: '',
    Authenticated: null
  },
  mutations: {
    Authenticated (state, If) {
      state.Authenticated = If
    },
    ApplyUserName (state, UserName) {
      state.UserName = UserName
    },
    ApplyToken (state, Token) {
      state.Token = Token
    },
    ApplyUserId (state, Id) {
      state.UserId = Id
    }
  }
})

new Vue({
  el: '#app',
  router,
  store: UserVuexStore,
  template: '<App/>',
  components: {index},
  render: h => h(index)
})
