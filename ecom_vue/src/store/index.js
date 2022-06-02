import { createStore } from "vuex";

export default createStore({
  state: {
    cart: {
      items: [],
    },
  },
  mutations: {
    addToCart(state, item) {
      const exists = state.cart.items.filter(
        (i) => i.productdetail.id === item.productdetail.id
      );
      console.log(exists.length);
      if (exists.length) {
        exists[0].quantity =
          parseInt(exists[0].quantity) + parseInt(item.quantity);
      } else {
        state.cart.items.push(item);
      }

      localStorage.setItem("cart", JSON.stringify(state.cart));
      console.log(localStorage);
    },
  },
  actions: {},
  modules: {},
});
