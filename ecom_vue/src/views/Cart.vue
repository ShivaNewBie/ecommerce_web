<template>
  <table class="content-table" v-if="cartTotalLength">
    <thead>
      <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Quantity</th>
        <th>Total price</th>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in cart.items" v-bind:key="item.productdetail.id">
        <td>
          <!-- <router-link :to="item.productdetail.get_absolute_url">{{
        item.productdetail.name
      }}</router-link> -->
          <router-link
            class="has-text-black"
            :to="item.productdetail.get_absolute_url"
            >{{ item.productdetail.name }}</router-link
          >
        </td>
        <td>${{ item.productdetail.price }}</td>
        <td>
          {{ item.quantity }}
          <button @click="decrementQuantity(item)">-</button>
          <button @click="incrementQuantity(item)">+</button>
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
      </tr>
    </tbody>
  </table>
  <p v-else>You don't have any products in your cart...</p>
</template>

<script>
// import CartItem from "@/components/CartItem.vue";

export default {
  name: "Cart",
  components: {
    // CartItem,
  },
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(
        (i) => i.productdetail.id !== item.productdetail.id
      );
    },
    getItemTotal(item) {
      return item.quantity * item.productdetail.price;
    },
    decrementQuantity(item) {
      item.quantity -= 1;
      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }
      this.updateCart();
    },
    incrementQuantity(item) {
      item.quantity += 1;
      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    // removeFromCart(item) {
    //   this.$emit("removeFromCart", item);
    //   this.updateCart();
    //   console.log(item);
    // },
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity);
      }, 0);
    },
  },
};
</script>
<style>
a {
  color: inherit;
}
.content-table {
  border-collapse: collapse;
  margin: 25px 0;
  font-size: 0.9em;
  width: 100%;
  border-radius: 5px 5px 0 0;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.content-table thead tr {
  background-color: #009879;
  color: #ffffff;
  text-align: left;
  font-weight: bold;
}

.content-table th,
.content-table td {
  padding: 12px 15px;
}

.content-table tbody tr {
  border-bottom: 1px solid #dddddd;
}

.content-table tbody tr:nth-of-type(even) {
  background-color: #f3f3f3;
}

.content-table tbody tr:last-of-type {
  border-bottom: 2px solid #009879;
}

.content-table tbody tr.active-row {
  font-weight: bold;
  color: #009879;
}
</style>
