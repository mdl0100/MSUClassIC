<script setup>
  // import {ref} from 'vue'
  import {auth} from '@/firebase.js'  
  import { signOut, getAuth } from 'firebase/auth';
  import ToolOption from './ToolOption.vue'
  
  async function signout(){
    await signOut(auth).then(() => {
      console.log('signed out');
    }).catch((error) => {
      console.log(error);
    });
  }
</script>

<template>
  <div class='tool'>
    <ToolOption />
  </div>
</template>

<style scoped>
  .tool {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: center; */
    height: 100vh;
    padding-top: 2rem;
  }
</style>