<template>
  <div class="sub-container">
    <div class="box-1">
      <div class="image-container">
        <img v-bind:src="product.get_image" />
        <!--to get localhost and url of image itself-->
      </div>
      <p>{{ product.name }}</p>
      <p>{{ product.description }}</p>
      <p>{{ product.price }}</p>
      <router-link v-bind:to="product.get_absolute_url" class="button is-dark"
        >View details</router-link
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "ProducList",
  props: {
    product: Object,
  },
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
