import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProductDetail from "../views/ProductDetail.vue";
import Cart from "../views/Cart.vue";
import Category from "../views/Category.vue";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import MyAccount from "../views/MyAccount.vue";

import { createArrayExpression } from "@vue/compiler-core";
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/:category_slug/:id/",
    name: "ProductDetail",
    component: ProductDetail,
  },
  {
    path: "/cart",
    name: "Cart",
    component: Cart,
  },
  {
    path: "/:category_slug",
    name: "Category",
    component: Category,
  },
  {
    path: "/log-in",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/my-account",
    name: "MyAccount",
    component: MyAccount,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  //user should be logged in order to access the url or component
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuthenticated
  ) {
    next("/log-in");
  } else {
    next();
  }
});
export default router;
