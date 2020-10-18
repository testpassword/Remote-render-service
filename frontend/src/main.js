import Vue from "vue"
import App from "./App.vue"
import Axios from "axios"
import router from '@/routes'

Vue.config.productionTip = false
Vue.prototype.$axios = Axios.create( {baseURL: "/api"} )

new Vue( {router, render: h => h(App)} ).$mount('#app')