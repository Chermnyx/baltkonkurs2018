import Vue from 'vue'
import App from './App'
import router from './router'
import Icon from './components/Icon.vue'

import 'materialize-css/dist/css/materialize.min.css'
import 'jquery'
import 'materialize-css/dist/js/materialize.min.js'

Vue.config.productionTip = false
Vue.component('icon', Icon)

window.store = new Vue({
  data: () => ({
    registrationForm: {
      firstName: null,
      lastName: null,
      sex: null
    },
    registerDone: false,
    test: {
      testUndone: true
    }
  })
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
