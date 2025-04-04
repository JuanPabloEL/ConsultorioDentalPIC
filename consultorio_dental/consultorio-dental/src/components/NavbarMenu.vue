<template>
    <div class="center examplex">
      <vs-navbar text-white color="#629bca" center-collapsed>
        
        <!-- Logo a la izquierda -->
        <template #left>
          <img src="logo-vuesax-logotipo-vuesax-png-4.png" alt="Logo" class="logo">
        </template>
  
        <!-- Menú de navegación -->
        <template #right>
          <vs-navbar-item>
            <router-link to="/">Inicio</router-link>
          </vs-navbar-item>
          
          
          <vs-navbar-item v-if="rol === 'dentista'">
            <router-link to="/pacientes">Citas</router-link>
          </vs-navbar-item>
  
          <vs-navbar-item v-if="rol === 'secretaria' || rol === 'dentista'">
            <router-link to="/citas">Gestionar Citas</router-link>
          </vs-navbar-item>
  
          <vs-navbar-item>
            <button @click="logout" class="logout-btn">Cerrar sesión</button>
          </vs-navbar-item>
        </template>
  
      </vs-navbar>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        rol: localStorage.getItem('rol') || ''
      };
    },
    methods: {
      logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('rol');
        this.$router.push('/login');
      }
    }
  }
  </script>
  
  <style scoped>
  /* Ajuste de la barra de navegación */
  .center {
    display: flex;
    justify-content: center;
    width: 100%;
  }
  
  .logo {
    height: 40px;
  }
  
  /* Estilos para el botón de cerrar sesión */
  .logout-btn {
    background: #00cbcc;
    border: none;
    color: white;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: 0.3s;
  }
  
  .logout-btn:hover {
    background: blue;
  }
  </style>
  