<template>
  <div id="content">
    <h1>{{ errorCode }}</h1>
    <h2>{{ errorMessage }}</h2>
    <router-link :to="redirectTo" class="illuminated">Вернуться на домашнюю страницу</router-link>
  </div>
</template>

<script>
export default {
  name: "NotFoundError",
  props: {
    errorCode: {
      type: String,
      required: true
    },
    errorMessage: {
      type: String,
      default: ""
    },
    redirectTo: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 8em;
  margin: 0;
  background: linear-gradient(130deg, #2a48eb, #ff0018);
  color: transparent;
  background-clip: text;
  text-transform: uppercase;
}

h2 {
  font-size: 33px;
  font-weight: 200;
  text-transform: uppercase;
  margin: 0;
  letter-spacing: 3px;
}
</style>