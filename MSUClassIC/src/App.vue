<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Login from './components/Login.vue'
import Site from './components/Site.vue'



</script>

<template>
  <header>
    <img alt="MSUClassIC logo" class="logo" src="@/assets/logo.png" width="125" height="125" />
   <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/site">Site</RouterLink>
        <span v-if="isLoggedIn"
        >>
        <button @click="signOut">Logout</button>
      </span>
      <span v-else>
        <router-link to="/Login"> Login </router-link> 
      </span>
      </nav>
    </div>
  </header>

  <RouterView />

</template>

<style scoped>
 header {
  line-height: 2;
  max-height: 100vh;
  width: 100%;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}


@media (min-width: 1024px) {
  header {
    display: flex;
    align-items: center;

  } 

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    flex: 1;
    display: flex;
    justify-content: space-between;

    }

  nav {
    text-align: left;
    font-size: 1rem;
    padding: 1rem 0;
    margin-top: 1rem;
  }
} 
</style>
./components/Login.vue
