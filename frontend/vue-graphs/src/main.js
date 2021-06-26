import { createApp } from "vue";
import { createRouter, createWebHistory } from 'vue-router'
import App from "./App.vue";
import HelloWorld from "./components/HelloWorld.vue";
import GraphsPage from "./components/GraphsPage.vue";

const routes = [
  { path: "/", component: HelloWorld },
  { path: "/about", component: GraphsPage },
];

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHistory(),
  routes, // short for `routes: routes`
});

createApp(App).use(router).mount("#app");
