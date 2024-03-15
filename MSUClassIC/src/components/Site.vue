<script setup>
  // import {ref} from 'vue'
  import {auth} from '@/firebase.js'  
  import { signOut, getAuth } from 'firebase/auth';
  import ToolOption from './ToolOption.vue'
  import Grid from './Grid.vue';
  
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
  <div class="grid">
     <Grid />
  </div>
 
</template>

<style scoped>
  .tool {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: center; */
    padding-bottom: 2rem;
    padding-top: 2rem;
  }
  
  .grid {
    display: block;
    padding: 2rem;
  }
</style>