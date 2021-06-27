<template>
  <div>
    <h1>Gráficas</h1>

    <div id="layout">
      <Chart :type="graphType" :data="basicData" :options="basicOptions" />
      <div class="options">
        <p>Seleccione un tipo de gráfica:</p>
        <button @click="graphType = 'bar'">Bar chart</button>
        <button @click="graphType = 'horizontalBar'">
          Horizontal bar chart
        </button>
        <button @click="graphType = 'pie'">Pie chart</button>

        <hr>
        <p>Seleccione un estado:</p>
        <select v-model="estado">
          <option selected>Tabasco</option>
          <option>Veracruz</option>
          <option>Edo.Mex</option>
        </select> <br><br>
        <span>Seleccionaste: {{ estado }}</span>
        <br>
        <button v-if="estado != ''" @click="graphType = 'horizontalBar'">
          Horizontal bar chart
        </button>

        <hr>
        <p>Seleccione un tipo de gráfica:</p>
        <button @click="graphType = 'bar'">Bar chart</button>
        <button @click="graphType = 'horizontalBar'">
          Horizontal bar chart
        </button>
        <button @click="graphType = 'pie'">Pie chart</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      graphType: "bar",
      estado: "",
      basicData: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "My First dataset",
            backgroundColor: "#42A5F5",
            data: [65, 59, 80, 81, 56, 55, 40],
          },
          {
            label: "My Second dataset",
            backgroundColor: "#FFA726",
            data: [28, 48, 40, 19, 86, 27, 90],
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

.p-chart {
  width: 50%;
}
.options {
  width: 50%;
}
</style>
