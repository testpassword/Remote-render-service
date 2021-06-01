<template>
  <div id="header" class="shaded animated">
    <h1>{{ title }}</h1>
    <table id="credit">
      <tbody>
      <tr>
        <td><img v-bind:src="authorLogoPath" alt="Лого разработчика"></td>
        <td><a class="illuminated" v-bind:href="authorUrl" title="Перейти на сайт разработчика">{{ authorName }}</a></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Vue from "vue"

export default {
  name: "Header",
  props: {
    title: {
      type: String,
      default: Vue.name
    },
    authorName: {
      type: String,
      default: ""
    },
    authorUrl: {
      type: String,
      default: ""
    },
    authorLogoPath: {
      type: String,
      required: false
    }
  }
}
</script>

<style scoped>
#header {
  font-size: 0.6em;
  top: 0;
  left: 0;
  z-index: 10; /*чтобы header всегда был сверху*/
  width: 100%;
  position: fixed;
  color: white;
  background-color: #000720;
}

#credit { margin: auto }

#credit img {
  width: 40px;
  height: 40px;
}

#credit a {
  font-size: 15px;
  text-decoration: none;
  color: white;
}

h1 {
  text-transform: uppercase;
  letter-spacing: 3px;
}
</style>