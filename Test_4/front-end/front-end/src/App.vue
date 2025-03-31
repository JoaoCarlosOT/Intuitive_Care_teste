<template>
  <div id="app">
    <HelloWorld /> <!-- Este é o componente HelloWorld com a mensagem inicial -->
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';  // Importa o componente HelloWorld

export default {
  components: {
    HelloWorld,  // Define o componente HelloWorld
  }
};
</script>
