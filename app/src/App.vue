<script>
import {mapActions, mapState} from "vuex";
export default {
  computed: mapState({
    isAuth: state => state.auth.isAuth
  }),
  methods: {
    ...mapActions({
      logout: 'logout',
    })
  }
}
</script>
<template>
  <nav>
    <router-link to="/" class="btn btn-primary nav-item">Главная</router-link>
    <router-link to="/profile" class="btn btn-primary nav-item">Профиль</router-link>
    <router-link to="/products" class="btn btn-primary nav-item">Товары</router-link>
    <wave-button v-if="isAuth" @click="logout()" class="nav-item">Выйти</wave-button>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
nav {
  padding-top: 5px;
}
.nav-item {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  margin: 0px 10px;
}

.form-header{
    margin-bottom: 10px;
}
.form-button {
    margin-top: 10px;
}
.default-form {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-content: center;
    justify-content: center;
    /* align-items: flex-start; */
    height: 85vh;
    max-width: 700px;
    margin: 10vh auto;
    box-shadow: 0 0 10px rgba(0, 68, 255, 0.5); 
    border-radius: 20px; 
    padding: 20px;
}
</style>
