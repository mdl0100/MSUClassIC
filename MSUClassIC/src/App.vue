<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import { RouterLink, RouterView } from 'vue-router';
import Login from './components/Login.vue';
import { onAuthStateChanged } from 'firebase/auth';
import { auth } from '@/firebase.js';
import router from './router';

const store = useStore();
const user = ref(null);

onAuthStateChanged(auth, currentUser => {
  if (currentUser) {
    store.commit('setUser', {
      email: currentUser.email,
      uid: currentUser.uid
    });
    user.value = currentUser; // Store user object locally for quick access
  } else {
    store.commit('clearUser');
    user.value = null;
  }
});

// Computed property to determine if user is authenticated
const isAuthenticated = computed(() => store.getters.isUserAuthenticated);

function signout() {
  auth.signOut().then(() => {
    router.push('/');
    console.log('signed out');
  }).catch((error) => {
    console.error('Error signing out:', error);
  });
}
</script>

<template>
  <header>
    <img alt="MSUClassIC logo" class="logo" src="@/assets/logo.png" width="125" height="125" @click="router.push('/')"/>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/site" v-if="isAuthenticated">Scheduler</RouterLink>
        <button v-if="isAuthenticated" @click="signout">Sign Out</button>
      </nav>
    </div>
  </header>

  <Login v-if="!isAuthenticated" />

  <RouterView />
</template>

<style scoped>
header {
  line-height: 2;
  max-height: 100vh;
  width: 100%;
  padding-top: 1rem;
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

@media (min-width: 2080px) {
  header {
    display: flexbox;
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

.form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

input {
  margin: 1rem;
  padding: 0.5rem;
  font-size: 1.5rem;
}

button {
  margin: 1rem;
  font-size: 1rem;
  align-items: center;
}

welcome {
  font-size: 2rem;
  text-align: center;
}
</style>
