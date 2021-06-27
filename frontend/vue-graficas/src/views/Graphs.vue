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
          <ProgressSpinner v-if="loadingOptions" />
        <div v-if="!loadingOptions">
            <p>Seleccione un tipo de gráfica:</p>
          <Button label="Bar chart" @click="graphType = 'bar'" class="p-button-warning"/>
          <Button label="Horizontal bar chart" @click="graphType = 'horizontalBar'" class="p-button-warning"/>
          <Button label="Pie chart" @click="graphType = 'pie'" class="p-button-warning"/>

          <hr />
          <p>Seleccione un estado:</p>
          <select v-model="estado">
              <option v-for="estado in estadosList" :key="estado"> {{estado}} </option>
          </select>
          <p>Mayor o menor # de vehículos:</p>
          <select v-model="reqOrder2">
            <option selected>Mayor</option>
            <option >Menor</option>
          </select>
          <br /><br />
          <span>Seleccionaste: {{ estado }}</span>
          <br />
          <Button v-if="estado != '' && reqOrder2 == 'Mayor' " label="Municipios con mayor número de vehículos de este estado" @click="getProblema('Municipios con mayor número de vehículos de: ' + estado, '2/' + estado )"  class="p-button-secondary" />
          <Button v-if="estado != '' && reqOrder2 == 'Menor' " label="Municipios con menor número de vehículos de este estado" @click="getProblema('Municipios con menor número de vehículos de: ' + estado, '8/' + estado )"  class="p-button-success" />

          <hr />
          <p>Seleccione una marca:</p>
          <select v-model="marca">
            <option v-for="nomMarca in marcasList" :key="nomMarca"> {{nomMarca}} </option>
          </select>
          <p>Mayor o menor # de vehículos:</p>
          <select v-model="reqOrder">
            <option selected>Mayor</option>
            <option >Menor</option>
          </select>
          <br /><br />
          <span>Seleccionaste: {{ marca }}</span>
          <br />
          <Button v-if="marca != '' && reqOrder == 'Mayor' " label="Modelos con mayor número de vehículos de esta marca" @click="getProblema('Modelos con mayor número de vehículos de: ' + marca, '5/' + marca )"  class="p-button-secondary" />
          <Button v-if="marca != '' && reqOrder == 'Menor' " label="Modelos con menor número de vehículos de esta marca" @click="getProblema('Modelos con menor número de vehículos de: ' + marca, '11/' + marca )"  class="p-button-success" />


          <hr />
          <p>Seleccione un problema:</p>
          <div id="buttonSet">
            <Button label="Estados con mayor número de vehículos" @click="getProblema('Estados con mayor número de vehículos', 1)"/>

            <Button label="Marcas con mayor número de vehículos" @click="getProblema('Marcas con mayor número de vehículos', 3)"/>
            <Button label="Colores con mayor número de vehículos" @click="getProblema('Colores con mayor número de vehículos', 4)"/>

            <Button label="Año en el que más vehículos se fabricaron" @click="getProblema('Año en el que más vehículos se fabricaron', 6)"/>
            
            <br>
            <Button label="Estados con menor número de vehículos" @click="getProblema('Estados con menor número de vehículos', 7)" class="p-button-help"/>

            <Button label="Marcas con menor número de vehículos" @click="getProblema('Marcas con menor número de vehículos', 9)" class="p-button-help"/>
            <Button label="Colores con menor número de vehículos" @click="getProblema('Colores con menor número de vehículos', 10)" class="p-button-help"/>

            <Button label="Año en el que menos vehículos se fabricaron" @click="getProblema('Año en el que menos vehículos se fabricaron', 12)" class="p-button-help"/>
          </div>
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
      reqOrder:"",
      reqOrder2:"",
      marca: "",
      loading: false,
      loadingOptions: false,
      marcasList: [],
      estadosList: [
        "Aguascalientes",
        "Baja California Norte",
        "Baja California Sur",
        "Campeche",
        "Coahuila de Zaragoza",
        "Colima",
        "Chiapas",
        "Chihuahua",
        "Distrito Federal",
        "Durango",
        "Guanajuato",
        "Guerrero",
        "Hidalgo",
        "Jalisco",
        "México",
        "Michoacán de Ocampo",
        "Morelos",
        "Nayarit",
        "Nuevo León",
        "Oaxaca",
        "Puebla",
        "Querétaro de Arteaga",
        "Quintana Roo",
        "San Luis Potosí",
        "Sinaloa",
        "Sonora",
        "Tabasco",
        "Tamaulipas",
        "Tlaxcala",
        "Veracruz",
        "Yucatán",
        "Zacatecas",
      ],
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
  mounted() {
  this.$nextTick(function () {
    this.loadingOptions = true;
    fetch("http://localhost:5000/marcasList")
        .then((response) => response.json())
        .then(async (data) => {
          console.log(await data);

          data.forEach((element) => {
            this.marcasList.push(element.data);
          });
          this.loadingOptions = false;
        })
        .catch((error) => {
          this.loadingOptions = false;

          console.error("There was an error on getting the Brand names!!", error);
        });
  })
}
};
</script>

<style scoped>
button {
  margin: 5px;
}

#layout {
  display: flex;
  justify-content: center;
}

#buttonSet > button,
.fromState {
  width: 80%;
}

button {
  padding: 5px;
}

#card1 {
  width: 60% !important;
}
#card2 {
  width: 30% !important;
  max-height: 75vh;
  overflow: scroll;
}
</style>
