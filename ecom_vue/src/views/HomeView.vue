<template>
  <div class="home">
    <div class="container-1">
      <img
        class="home-pic"
        :src="require(`@/assets/hossein-azarbad-AP_qief3n94-unsplash.jpg`)"
      />
      <div class="welcome">
        <p class="title mb-6 has-text-white">Welcome to caps</p>
        <p class="subtitle has-text-white">The best caps store online</p>
      </div>
    </div>
    <div class="container-2">
      <div class="is-size-2 has-text-centered">Latest Products</div>
      <div class="sub-container">
        <ProductList
          v-for="product in productList"
          v-bind:key="product.id"
          v-bind:product="product"
        />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import ProductList from "@/components/ProductList";

export default {
  name: "HomeView",
  components: {
    ProductList,
  },
  data() {
    return {
      productList: [],
    };
  },
  mounted() {
    this.getProductList();
  },
  methods: {
    getProductList() {
      axios
        .get("/api/v1/product-list/")
        .then((response) => {
          this.productList = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.home-pic {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 80%;
  height: 500px;
  padding-top: 30px;
}

.container-1 {
  position: relative;
  text-align: center;
  color: white;
  margin-bottom: 45px;
}

.welcome {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.container-2 {
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}
.sub-container {
  display: flex;
  justify-content: space-between;
}
</style>
