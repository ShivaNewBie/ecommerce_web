import { createStore } from "vuex";

export default createStore({
  state: {
    isLoading: false,

    token: "",
    isAuthenticated: false,

    user: {
      id: 0,
      username: "",
    },
    cart: {
      items: [],
    },
  },
  mutations: {
    initializeStore(state) {
      //this function only inializes an if statement not change any data rather it checks whether the data is authenticated
      if (localStorage.getItem("token")) {
        //token determines if the user is authenticated
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
        state.user.username = localStorage.getItem("username");
        state.user.id = localStorage.getItem("userid");
      }
    },
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
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    setToken(state, token) {
      state.token = token;
    },
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {},
  modules: {},
});
