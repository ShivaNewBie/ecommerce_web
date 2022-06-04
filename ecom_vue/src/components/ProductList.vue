<template>
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
</template>

<script>
export default {
  name: "ProducList",
  props: {
    product: Object,
  },
};
</script>

<style>
.box-1 {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* this adds the "card" effect */
  background-color: #f1f1f1;
  min-width: 20%;
  padding: 16px;
  margin: auto;
}
.box-1 img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  margin: auto;
}
.image-container {
  height: 300px;
  width: 200px;
  margin: auto;
}
</style>
