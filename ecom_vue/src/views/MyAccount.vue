<template>
  <h1>My account</h1>
  {{ $store.state.user }}
  {{ $store.state.isAuthenticated }}
</template>

<script>
export default {
  name: "MyAccount",
};
</script>
