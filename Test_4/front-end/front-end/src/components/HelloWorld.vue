<template>
  <div>
    <h1>Operadoras de Saúde</h1>

    <table v-if="operadoras.length > 0">
      <thead>
        <tr>
          <th>Dados da API</th>
        </tr>
      </thead>
      <tbody>
        <td>{{ operadoras }}</td>
      </tbody>
    </table>

    <p v-else>Sem dados encontrados</p>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      operadoras: [],
      loading: true
    };
  },
  created() {
    axios
      .get('http://127.0.0.1:5000/operadoras')
      .then(response => {
        console.log("Dados da API:", response.data);
        this.operadoras = response.data;
        this.loading = false;
      })
      .catch(err => {
        console.error('Erro ao carregar os dados', err);
        this.loading = false;
      });
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  color: black;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
</style>
