<template>
  <Menubar :model="items" />
  <router-view />
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          label: "Home",
          icon: "pi pi-fw pi-home",
          to: "/"
        },
        {
          label: "Gráficas",
          icon: "pi pi-fw pi-chart-bar",
          to: "/graphs"
        },
      ],
    };
  },
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
