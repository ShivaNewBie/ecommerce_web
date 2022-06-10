<template>
  <div class="cart-container">
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
          <td>
            <button class="delete" @click="removeFromCart(item)"></button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-else class="test-width">You don't have any products in your cart...</p>
    <div class="cart-container-2">
      <h2 class="subtitle">Summary</h2>

      <strong>${{ cartTotalPrice.toFixed(2) }}</strong
      >, {{ cartTotalLength.toFixed(2) }} items

      <hr />

      <router-link to="/checkout" class="button is-dark"
        >Proceed to checkout</router-link
      >
    </div>
  </div>
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
      //always check object name got stuck here should be productdetail not product
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.productdetail.price * curVal.quantity);
      }, 0);
    },
  },
};
</script>
<style>
a {
  color: inherit;
}
.cart-container {
  width: 80%;
  margin: auto;
}
.cart-container-2 {
  width: 100%;
}
.content-table {
  border-collapse: collapse;
  margin: auto;
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
.checkout-button {
  float: right;
}
</style>
