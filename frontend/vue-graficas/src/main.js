import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import PrimeVue from "primevue/config";

//  PrimeVue elements
import "primevue/resources/themes/saga-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";

import Chart from "primevue/chart";
import Card from "primevue/card";
import Button from 'primevue/button';
import ProgressSpinner from 'primevue/progressspinner';

const app = createApp(App);
app.use(PrimeVue, { ripple: true });
app.use(router);

app.component("Chart", Chart);
app.component("Card", Card);
app.component("Button", Button);
app.component("ProgressSpinner", ProgressSpinner);

app.mount("#app");
