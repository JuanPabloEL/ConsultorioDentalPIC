<template>
    <div class="login-container">
      <div class="login-box">
        <h2>Inicio de Sesión</h2>
        <form @submit.prevent="login">
          <label>Email</label>
          <input type="text" v-model="email" required />          
          <label>Contraseña</label>
          <input type="password" v-model="password" required />
          
          <button type="submit">Ingresar</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        email: '',
        password: ''
      }
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/usuarios/login/', {
            email: this.email,
            password: this.password
          })
          localStorage.setItem('token', response.data.access)
          localStorage.setItem('rol', response.data.rol)
          this.$router.push('/')
        } catch (error) {
          alert('Error al iniciar sesión')
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .login-container {
    background: url('https://img.freepik.com/foto-gratis/vacie-oficina-hospital-estomatologia-dental-moderna-nadie-el-equipado-instrumentos-dentales-listos-tratamiento-medico-ortodoncista-imagenes-radiografia-dental-exhibicion_482257-9418.jpg') no-repeat center center/cover;
    position: relative;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
  }
  
  /* Efecto de desenfoque */
  .login-container::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
  }
  
  /* Caja de inicio de sesión */
  .login-box {
    position: relative;
    background: #629bca;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
    text-align: center;
    color: white;
    max-width: 400px;
    width: 100%;
    border: none;
    outline: none;
  }
  
  /* Campos de entrada */
  .login-box input {
    width: 100%;
    padding: 12px;
    margin: 10px 0;
    border: none;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.2);
    color: white;
  }
  
  /* Estilo para el placeholder */
  .login-box input::placeholder {
    color: rgba(255, 255, 255, 0.7);
  }
  
  /* Botón */
  .login-box button {
    width: 100%;
    padding: 12px;
    border: none;
    border-radius: 5px;
    background: #00cbcc;
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
  }
  
  .login-box button:hover {
    background: blue;
  }


  </style>
  