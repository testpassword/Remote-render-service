<template>
  <h3><span class="notification stub" v-if="isVisible" :class="{ errorStub: isError }">{{ message }}</span></h3>
</template>

<script>
export default {
  name: "Notification",
  props: {
    isError: {
      type: Boolean,
      default: false
    },
    isVisible: {
      type: Boolean,
      default: true
    },
    message: {
      type: String,
      default: ""
    }
  }
}
</script>

<style scoped>
.notification {
  color: white;
  padding: 10px;
}

.stub { background-color: #000720 }

.errorStub { background-color: #dc143b }
</style>