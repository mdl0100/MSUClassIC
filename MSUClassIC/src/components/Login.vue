<script setup>
  import {auth} from '@/firebase.js'
  import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from 'firebase/auth';
  import { ref } from 'vue';

  const data = ref({
    email: '',
    password: ''
  });

  const mode = ref('login');
  const user = ref(null);

  function
    toggleMode(val){
    mode.value = val;
  }

  async function login(email, password){
    await signInWithEmailAndPassword(auth, email, password).then((res) => {
      console.log(res);
    }).catch((error) => {
      console.log(error);
    });
  }

  async function register(email, password){
    await createUserWithEmailAndPassword(auth, email, password).then((res) => {
      console.log(res);
    }).catch((error) => {
      console.log(error);
    });
  }

  function submit(){
    let email = data.value.email;
    let password = data.value.password;
    if (mode.value === 'login'){
      login(email, password);
    } else {
      register(email, password);
    }
  }

  async function signout(){
    await signOut(auth).then(() => {
      console.log('signed out');
    }).catch((error) => {
      console.log(error);
    });
  }

  onAuthStateChanged(auth, currentUser => {
    user ? user.value = currentUser : user.value = null;
    this.$emit('user', user.value);
  });
</script>

<template>
  <div>
    <div class="welcome" v-if="user">Welcome {{user.email}} <br/><button @click="signout">Sign Out</button></div>
    <form v-else @submit.prevent="submit">
      <div>
        <input v-model="data.email" type="email" placeholder="Email" />
      </div> 
      <div>
        <input v-model="data.password" type="password" placeholder="Password" />
      </div>
      <button type="submit">{{mode ==='login' ? 'Login' : "Register"}}</button>
      <div @click="toggleMode(mode ==='login' ? 'register' : 'login')">
        {{ mode === 'login' ? 'Need an account?' : 'Already have a user? Login' }}
      </div>
    </form>
  </div>
</template>

<style scoped>
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
    padding: 0.5rem;
    font-size: 1.5rem;
    align-items: center;
  }

  .welcome {
    font-size: 2rem;
    text-align: center;
  }
</style>