<template>
  <div>
    <Navbar  v-if="showNavbar"/>
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/NavbarMenu.vue';
import { useRoute } from 'vue-router';
import { ref, watchEffect } from 'vue';
export default {
  components: { Navbar },
  setup(){
    const route = useRoute();
    const showNavbar = ref(route.path !== '/login');

    // Reactualiza la visibilidad de la Navbar al cambiar de ruta
    watchEffect(() => {
      showNavbar.value = route.path !== '/login';
    });

    return { showNavbar };
  }
  
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
