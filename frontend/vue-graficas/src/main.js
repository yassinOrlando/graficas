import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import PrimeVue from "primevue/config";

//  PrimeVue elements
import "primevue/resources/themes/saga-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";

import Chart from "primevue/chart";

const app = createApp(App);
app.use(PrimeVue, { ripple: true });
app.use(router);
app.component("Chart", Chart);

app.mount("#app");
