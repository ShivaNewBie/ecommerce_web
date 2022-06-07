<template>
  <div class="product-detail-container mt-6">
    <div class="product-detail-box-1">
      <figure><img v-bind:src="productdetail.get_image" alt="" /></figure>
    </div>

    <div class="product-detail-box-2">
      <h1 class="title mb-5">{{ productdetail.name }}</h1>
      <h1 class="subtitle mb-2">
        {{ productdetail.description }}
      </h1>
      <h1 class="subtitle mb-2">{{ productdetail.price }}</h1>

      <div class="">
        <div class="addon-input control">
          <input
            type="number"
            class="input mb-2"
            size="5"
            min="1"
            v-model="quantity"
          />
        </div>

        <div class="control">
          <a class="button is-dark" @click="addToCart()">Add to cart</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "ProductDetail",
  data() {
    return {
      productdetail: {},
      quantity: 1,
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      const category_slug = this.$route.params.category_slug;
      const id = this.$route.params.id; //reference to vue router

      await axios
        .get(`api/v1/product/${category_slug}/${id}/`)
        .then((response) => {
          this.productdetail = response.data;
          console.log(response.data);
          document.title = this.productdetail.name + " | Caps";
        });
    },
    addToCart() {
      //this is where our cart gets data
      const item = {
        productdetail: this.productdetail,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", item);
      toast({
        message: "The product was added to the cart",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
    },
  },
};
</script>

<style>
.product-detail-container {
  display: flex;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* this adds the "card" effect */
  background-color: #f1f1f1;
  min-width: 20%;
  padding: 50px;
  margin: auto;
  width: 50%;
}
.product-detail-container div {
}
img {
  width: 400px;
  height: 300px;
}

.product-detail-box-1 {
  flex: 1;
}
.product-detail-box-2 {
  flex: 1;
  margin-right: auto;
  margin-left: auto;
  text-align: center;
}
.addon-input {
  width: 70px;
  text-align: center;
  margin-right: auto;
  margin-left: auto;
}
</style>
