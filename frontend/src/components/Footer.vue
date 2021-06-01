<template>
  <div id="footer" class="shaded animated">
    <figure>
      <a class="illuminated" v-bind:href="url">
        <img v-bind:src="logoPath" alt="Лого компании" title="Перейти на сайт компании" class="illuminated">
      </a>
      <figcaption>{{ devYear.getFullYear() }}</figcaption>
    </figure>
  </div>
</template>

<script>
export default {
  name: "Footer",
  props: {
    logoPath: {
      type: String,
      required: true
    },
    url: {
      type: String,
      required: true
    },
    devYear: {
      type: Date,
      default: Date()
    }
  }
}
</script>

<style scoped>
#footer {
  bottom: 0;
  z-index: 10; /*чтобы footer всегда был сверху*/
  width: 100%;
  position: fixed;
  color: white;
  background-color: #000720;
  left: 0;
}

figure img { height: 35px }

figcaption {
  font-size: 0.8em;
  display: block;
}

figure { padding: 0.5% }
</style>