
<script setup>
import { RouterLink, RouterView } from 'vue-router' // For navigtion bar
//No longer used, now incorporated into App.vue
  // import Login from './components/Login.vue' 
import Site from './components/Site.vue'            // For the site page

import {auth} from '@/firebase.js'                  // For authentication of Users    
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from 'firebase/auth';
import { ref } from 'vue';                          
import router from './router';                      // For routing to different pages          
// import UserAuth from './components/UserAuth';

// const userAuth = new UserAuth();
// userAuth.router = router;

// const {user, data, mode } = userAuth;
// const {login, register, submit, signout} = userAuth;


const data = ref({
  email: '',
  password: '',
  department: ''
});

const mode = ref('login');
const user = ref(null);

function
    toggleMode(val){
    mode.value = val;
  }


// 
async function login(email, password){
  await signInWithEmailAndPassword(auth, email, password).then((res) => {
    console.log(res);
  }).catch((error) => {
    console.log(error);
  });
  // If user is logged in, redirect to site page
  // Also pull the user's data from the database
  if (user.value){
    fetchUserData();
    router.push('/site');
  }
}

async function register(email, password, department){
  await createUserWithEmailAndPassword(auth, email, password).then((res) => {
    console.log(res)
    let token = res;
  }).catch((error) => {
    console.log(error);
  });
  // If registering, send user token and department to the database
  console.log(email);
  console.log(department);

}

// On submit, the user will either login or register
function submit(){
  let email = data.value.email;
  let password = data.value.password;
  let department = data.value.department;
  if (mode.value === 'login'){
    login(email, password);
  } else {
    register(email, password, department);
  }
}

// Signout the user
async function signout(){
  await signOut(auth).then(() => {
    console.log('signed out');
  }).catch((error) => {
    console.log(error);
  });
  router.push('/');
}

//NOT DONE
function fetchUserData(){
  // Fetch user data from the database
  // This will be used to populate the site page
  console.log('fetching user data');
}


onAuthStateChanged(auth, currentUser => {
  user ? user.value = currentUser : user.value = null;
});
</script>


<template>


  <header>
    <img alt="MSUClassIC logo" class="logo" src="@/assets/logo.png" width="125" height="125" @click="router.push('/')"/>
   <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/site" v-if="user">Scheduler</RouterLink>
        <button v-if="user" @click="signout">Sign Out</button>
      </nav>

    </div>
  </header>
  <div>
    <!-- <div class="welcome" v-if="user">Welcome {{user.email}} </div> -->
    <form v-if="!user" @submit.prevent="submit">
      <div>
        <input v-model="data.email" type="email" placeholder="Email" />
      </div> 
      <div>
        <input v-model="data.password" type="password" placeholder="Password" />
      </div>
      <div v-if="mode !== 'login'">
        <input v-model="data.department" type="text" placeholder="Department" />
      </div>
      <button type="submit">{{mode ==='login' ? 'Login' : "Register"}}</button>
      <div @click="toggleMode(mode ==='login' ? 'register' : 'login')">
      {{ mode === 'login' ? 'Need an account? Register' : 'Already have a user? Login' }}
      </div>
    </form>
  </div> 
  <RouterView />
  

</template>

<style scoped>
 header {
  line-height: 2;
  max-height: 100vh;
  width: 100%;
  padding-top:1rem;
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


@media (min-width: 800px) {
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

form {
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

  .welcome {
    font-size: 2rem;
    text-align: center;
  }
</style>
./components/Login.vue
