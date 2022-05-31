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
        <li><router-link to="/">Sports</router-link></li>
        <li><router-link to="/">Fashion</router-link></li>
        <li><router-link to="/">My account</router-link></li>
        <li><router-link to="/">Cart</router-link></li>
      </ul>
    </nav>
  </div>

  <router-view />
</template>

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
}
</style>
