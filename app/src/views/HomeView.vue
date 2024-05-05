<template>
  <div class="home">
    <h1>Зарегистрироваться в системе как</h1>
    <wave-button @click="$router.push('/client')" class="b">Клиент</wave-button>
    <wave-button @click="$router.push('/maker')" class="b">Производитель</wave-button>
    <wave-button @click="$router.push('/distributor')" class="b">Дистрибутор</wave-button>
    <wave-button @click="$router.push('/operator')" class="b">Оператор</wave-button>
    <h2>Войти</h2>
    <wave-button @click="$router.push('/login')" class="b">Войти</wave-button>
  </div>
</template>

<script>

export default {
  name: 'HomeView',
}
</script>

<style scoped>
.b {
  margin: 0px 10px;
}
</style>