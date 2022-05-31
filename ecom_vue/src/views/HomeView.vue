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
        <div class="box-1">
          <div class="image-container">
            <img
              :src="require(`@/assets/erik-mclean-WIejoQqIvhE-unsplash.jpg`)"
              alt=""
            />
          </div>
          <p>box 1</p>
        </div>
        <div class="box-1">
          <div class="image-container">
            <img
              :src="
                require(`@/assets/claudio-schwarz-PH8GUKG-Do0-unsplash.jpg`)
              "
              alt=""
            />
          </div>
          <p>box 2</p>
        </div>
        <div class="box-1">
          <div class="image-container">
            <img
              :src="require(`@/assets/dave-goudreau-FEx5z_k0hss-unsplash.jpg`)"
              alt=""
            />
          </div>
          <p>box 3</p>
        </div>
        <div class="box-1" id="sad">
          <div class="image-container">
            <img
              :src="require(`@/assets/erik-mclean-WIejoQqIvhE-unsplash.jpg`)"
              alt=""
            />
          </div>
          <p>box 4</p>
        </div>
      </div>
    </div>
  </div>
  <br />
  <br />
  <br />
  <br />
</template>

<script>
// @ is an alias to /src

export default {
  name: "HomeView",
  components: {},
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
.box-1 {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* this adds the "card" effect */
  background-color: #f1f1f1;
  width: 20%;
  padding: 16px;
  margin: auto;
}
.box-1 img {
  height: 100%;
  width: 100%;
  object-fit: cover;
  margin: auto;
}
.image-container {
  height: 300px;
  width: 200px;
  margin: auto;
}
</style>
