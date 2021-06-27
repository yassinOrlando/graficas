<template>
  <div>
    <h1>Gráficas</h1>

    <div id="layout">
      <Card id="card1">
        <template #title> {{ title }} </template>
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
        <template #title> Opciones </template>
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
            <button @click="getProblema('Estados con mayor número de vehículos', 1)"> Estados con mayor número de vehículos </button>
            <button @click="getProblema('Municipios con mayor número de vehículos a revisar', '2/Tabasco')">Problema 2</button>
            <button @click="getProblema('Marcas con mayor número de vehículos', 3)">Marcas con mayor número de vehículos</button>
            <button @click="getProblema('Colores con mayor número de vehículos', 4)">Colores con mayor número de vehículos</button>
            <button @click="getProblema('Modelos con mayor número de vehículos a revisar', '5/Nissan')">Problema 5</button>
            <button @click="getProblema('Año en el que más vehículos se fabricaron', 6)">Año en el que más vehículos se fabricaron</button>
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
      title: "Datos de ejemplo",
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
          "July2",
          "July3",
          "July4",
        ],
        datasets: [
          {
            label: "Dataset",
            backgroundColor: [
              "#EC407A",
              "#AB47BC",
              "#42A5F5",
              "#444",
              "#66BB6A",
              "#FFCA28",
              "#26A69A",
              "red",
              "orange",
              "green",
            ],
            data: [65, 59, 80, 81, 56, 55, 40, 12, 56, 87],
          },
        ],
      },
      basicOptions: null,
    };
  },
  methods: {
    getProblema(title, actNum) {
      this.loading = true;
      this.title = title;

      fetch("http://localhost:5000/act" + actNum)
        .then((response) => response.json())
        .then(async (data) => {
          console.log(await data);
          this.basicData["labels"] = [];
          this.basicData["datasets"][0]["data"] = [];

          data.forEach((element) => {
            console.log(element);
            console.log(element["data"]);
            console.log(element["num_autos"]);
            this.basicData["labels"].push(element["data"]);
            this.basicData["datasets"][0]["data"].push(element["num_autos"]);
          });
          this.loading = false;
        })
        .catch((error) => {
          this.loading = false;

          console.error("There was an error!", error);
        });
    },
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
