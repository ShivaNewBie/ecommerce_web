<template>
  <div class="wrapper">
    <nav class="navbar">
      <div class="nav-start">
        <router-link to="/" class="test" id="test-me"
          ><strong>Caps</strong></router-link
        >
        <form class="test" method="get" action="/search">
          <div class="field has-addons">
            <div class="control">
              <input
                type="text"
                class="input"
                placeholder="What are you looking for?"
                name="query"
              />
            </div>

            <div class="control">
              <button class="button is-success">
                <span class="icon">
                  <i class="fas fa-search"></i>
                </span>
              </button>
            </div>
          </div>
        </form>
      </div>
      <ul class="nav-end">
        <div class="nice">
          <li><router-link to="/sports">Sports</router-link></li>
          <li><router-link to="/fashion">Fashion</router-link></li>

          <li>
            <router-link to="/cart">Cart: {{ cartTotalLength }} </router-link>
          </li>
        </div>
        <template class="nice" v-if="$store.state.isAuthenticated">
          <li>
            <router-link to="/my-account">My account</router-link>
          </li>

          <li>
            <button class="button is-danger" @click="logout()">Logout</button>
          </li>
        </template>
        <template v-else>
          <li><router-link to="/login">Log- in</router-link></li>
          <li><router-link to="/signup">Signup</router-link></li>
        </template>
      </ul>
    </nav>
    <div
      class="is-loading-bar has-text-centered"
      v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-dual-ring"></div>
    </div>
  </div>

  <router-view />
</template>
<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },
  beforeCreate() {
    //before code will run
    this.$store.commit("initializeStore"); //the commit will make initializeStore run or use the function

    if (this.$store.state.token) {
      //reference to the token
      axios.defaults.headers.common["Authorization"] =
        "Token " + this.$store.state.token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
        console.log(this.cart.items[i].quantity); //we get quantity object then add 1
      }
      return totalLength;
    },
  },
  methods: {
    logout() {
      axios
        .post("api/v1/token/logout/")
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");
      this.$store.commit("removeToken");

      this.$router.push("/");
    },
  },
};
</script>
<style lang="scss">
@import "../node_modules/bulma";

* {
  font-family: "Poppins", sans-serif;
}

.wrapper {
  width: 100%;
  height: 64px;
  background-color: #1d2518;
}
.navbar {
  height: 64px;
  max-width: 80%;
  background-color: #1d2518;
  color: #ffffff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
}
.nice {
  display: inline-block;
}

.nav-start .test {
  display: inline-block;
  // padding: 0px 20px;
  padding-right: 20px;
  vertical-align: middle;
}

.nav-end {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

a {
  color: #ffffff;
}
.nav-end li {
  display: inline-block; //side by side list
  padding-right: 20px;
  vertical-align: middle;
}
.lds-dual-ring {
  display: inline-block;
  width: 800px;
  height: 80px;
}

.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
