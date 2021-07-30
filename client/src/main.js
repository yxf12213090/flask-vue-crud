import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

// import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css'
//
import axios from './config/httpConfig';

Vue.prototype.$http = axios;

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
