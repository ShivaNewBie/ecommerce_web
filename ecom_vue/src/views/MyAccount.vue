<template>
  <h1>My account</h1>
  {{ $store.state.user }}
  {{ $store.state.isAuthenticated }}
  {{ $store.state.cart.items }}
</template>

<script>
export default {
  name: "MyAccount",
};
</script>
