<template>
  <div>
    <h1>Gráficas</h1>

    <div id="layout">
      <Card id="card1">
        <template #title> Advanced Card </template>
        <template #content>
          <div>
            <ProgressSpinner v-if="loading" />
            <Chart
              v-if="!loading"
              :type="graphType"
              :data="basicData"
              :options="basicOptions"
            />
          </div>
        </template>
      </Card>

      <Card id="card2">
        <template #title> Options </template>
        <template #content>
          <p>Seleccione un tipo de gráfica:</p>
          <button @click="graphType = 'bar'">Bar chart</button>
          <button @click="graphType = 'horizontalBar'">
            Horizontal bar chart
          </button>
          <button @click="graphType = 'pie'">Pie chart</button>

          <hr />
          <p>Seleccione un estado:</p>
          <select v-model="estado">
            <option selected>Tabasco</option>
            <option>Veracruz</option>
            <option>Edo.Mex</option>
          </select>
          <br /><br />
          <span>Seleccionaste: {{ estado }}</span>
          <br />
          <button
            class="fromState"
            v-if="estado != ''"
            @click="graphType = 'horizontalBar'"
          >
            Horizontal bar chart
          </button>

          <hr />
          <p>Seleccione una marca:</p>
          <select v-model="marca">
            <option selected>BMW</option>
            <option>Volkswagen</option>
          </select>
          <br /><br />
          <span>Seleccionaste: {{ marca }}</span>
          <br />
          <button
            class="fromState"
            v-if="marca != ''"
            @click="graphType = 'horizontalBar'"
          >
            Horizontal bar chart
          </button>

          <hr />
          <p>Seleccione un problema:</p>
          <div id="buttonSet">
            <button @click="console.log('Problema 1')">Problema 1</button>
            <button @click="console.log('Problema 2')">Problema 2</button>
            <button @click="console.log('Problema 3')">Problema 3</button>
            <button @click="console.log('Problema 4')">Problema 4</button>
            <button @click="console.log('Problema 5')">Problema 5</button>
            <button @click="console.log('Problema 6')">Problema 6</button>
          </div>
        </template>
      </Card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      graphType: "bar",
      estado: "",
      marca: "",
      loading: false,
      basicData: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "July",
          "July",
          "July",
        ],
        datasets: [
          {
            label: "My First dataset",
            backgroundColor: ['#EC407A','#AB47BC','#42A5F5','#444','#66BB6A','#FFCA28','#26A69A', 'red', 'orange', 'green'],
            data: [65, 59, 80, 81, 56, 55, 40, 12, 56, 87],
          },
        ],
      },
      basicOptions: null,
    };
  },
};
</script>

<style scoped>
button {
  margin: 5px;
}

#layout {
  display: flex;
}

#buttonSet > button,
.fromState {
  width: 50%;
}

button {
  padding: 5px;
}

#card1 {
  width: 65% !important;
}
#card2 {
  width: 35% !important;
}
</style>
